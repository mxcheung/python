from confluent_kafka import Consumer, KafkaException
import logging, sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def error_callback(err):
    logger.error(f"Kafka error: {err}")

conf = {
    'bootstrap.servers': 'broker:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
    'error_cb': error_callback,
}

consumer = Consumer(conf)
consumer.subscribe(['my-topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        logger.error(f"Message error on topic={msg.topic()} partition={msg.partition()} offset={msg.offset()}: {msg.error()}")
        continue
    try:
        value = msg.value().decode('utf-8')  # or your custom deserializer
        logger.debug(f"Consumed message from topic={msg.topic()} partition={msg.partition()} offset={msg.offset()}")
    except Exception as e:
        logger.exception(f"Deserialization failed on topic={msg.topic()} partition={msg.partition()} offset={msg.offset()}: {e}")