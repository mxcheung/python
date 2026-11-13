
# kafka_framework/consumer.py

import logging
import queue
import threading
import time

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from confluent_kafka import Consumer, KafkaException, TopicPartition


logger = logging.getLogger(__name__)


class KafkaBatchConsumer:

    def __init__(
        self,
        bootstrap_servers: str,
        group_id: str,
        max_workers: int = 10,
        auto_offset_reset: str = "earliest",
        poll_timeout: float = 0.2,
    ):

        self.consumer = Consumer({
            "bootstrap.servers": bootstrap_servers,
            "group.id": group_id,
            "auto.offset.reset": auto_offset_reset,
            "enable.auto.commit": False,
            "enable.auto.offset.store": False,
        })

        self.executor = ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix="kafka-worker",
        )

        self.poll_timeout = poll_timeout

        # Topic configuration and handlers
        self.handlers = {}

        # Messages grouped by topic and partition
        self.buffers = defaultdict(list)
        self.first_message_at = {}

        # Partitions currently processing
        self.in_flight = set()

        # Worker completion notifications
        self.completed = queue.Queue()

        self.stop_event = threading.Event()

    # --------------------------------------------------
    # Register topic handler
    # --------------------------------------------------

    def register(
        self,
        topic: str,
        handler,
        batch_size: int = 100,
        flush_interval: float = 2,
    ):

        if topic in self.handlers:
            raise ValueError(f"Duplicate topic: {topic}")

        if batch_size < 1 or flush_interval <= 0:
            raise ValueError("Invalid batch configuration")

        self.handlers[topic] = {
            "handler": handler,
            "batch_size": batch_size,
            "flush_interval": flush_interval,
        }

    # --------------------------------------------------
    # Submit batch to thread pool
    # --------------------------------------------------

    def _submit_batch(self, key, messages):

        topic, partition = key
        handler = self.handlers[topic]["handler"]

        self.consumer.pause([
            TopicPartition(topic, partition)
        ])

        self.in_flight.add(key)

        future = self.executor.submit(
            handler.process_batch,
            messages,
        )

        future.add_done_callback(
            lambda f, k=key, m=messages:
                self.completed.put((k, m, f))
        )

        logger.info(
            "Batch submitted topic=%s partition=%s count=%d",
            topic, partition, len(messages)
        )

    # --------------------------------------------------
    # Dispatch buffered batches
    # --------------------------------------------------

    def _dispatch_batches(self, force=False):

        now = time.monotonic()

        for key, messages in list(self.buffers.items()):

            if not messages or key in self.in_flight:
                continue

            topic, partition = key
            config = self.handlers[topic]

            batch_ready = (
                len(messages) >= config["batch_size"]
            )

            timeout = (
                now - self.first_message_at[key]
                >= config["flush_interval"]
            )

            if force or batch_ready or timeout:

                batch = messages.copy()

                self.buffers[key].clear()
                self.first_message_at.pop(key, None)

                self._submit_batch(key, batch)

    # --------------------------------------------------
    # Process completed batches
    # --------------------------------------------------

    def _process_completed(self):

        while True:

            try:
                key, messages, future = (
                    self.completed.get_nowait()
                )
            except queue.Empty:
                break

            topic, partition = key

            try:

                # Raise any worker exception
                future.result()

                next_offset = messages[-1].offset() + 1

                # Commit only after successful processing
                result = self.consumer.commit(
                    offsets=[
                        TopicPartition(
                            topic,
                            partition,
                            next_offset,
                        )
                    ],
                    asynchronous=False,
                )

                if result:
                    for committed in result:
                        if committed.error:
                            raise KafkaException(committed.error)

                logger.info(
                    "Batch completed topic=%s partition=%s "
                    "count=%d offset=%d",
                    topic,
                    partition,
                    len(messages),
                    next_offset,
                )

                self.in_flight.remove(key)

                self.consumer.resume([
                    TopicPartition(topic, partition)
                ])

            except Exception:
                logger.exception(
                    "Batch failed topic=%s partition=%s",
                    topic, partition,
                )

                # Do not commit failed messages.
                # Stop processing rather than lose messages.
                raise

    # --------------------------------------------------
    # Main consumer loop
    # --------------------------------------------------

    def start(self):

        if not self.handlers:
            raise ValueError("No handlers registered")

        topics = list(self.handlers.keys())

        logger.info("Subscribing to topics: %s", topics)

        self.consumer.subscribe(topics)

        try:

            while (
                not self.stop_event.is_set()
                or self.in_flight
                or any(self.buffers.values())
            ):

                # Check worker completion
                self._process_completed()

                # Poll Kafka
                message = self.consumer.poll(
                    self.poll_timeout
                )

                if message is not None:

                    if message.error():
                        raise KafkaException(message.error())

                    key = (
                        message.topic(),
                        message.partition(),
                    )

                    if not self.buffers[key]:
                        self.first_message_at[key] = (
                            time.monotonic()
                        )

                    self.buffers[key].append(message)

                # Dispatch ready batches
                self._dispatch_batches(
                    force=self.stop_event.is_set()
                )

        except KeyboardInterrupt:
            logger.info("Shutdown requested")

        finally:

            self.executor.shutdown(wait=True)
            self.consumer.close()

    # --------------------------------------------------
    # Graceful shutdown request
    # --------------------------------------------------

    def stop(self):
        self.stop_event.set()
