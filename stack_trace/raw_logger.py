import os
import logging
import traceback
from aws_lambda_powertools import Logger

# Enable Powertools for structured logging
logger = Logger(service="payment-service")

# Set up default Python logger for raw tracebacks
raw_logger = logging.getLogger("raw")
raw_logger.setLevel(logging.ERROR)

def lambda_handler(event, context):
    try:
        # Structured log example
        logger.info("Processing event", extra={"event_id": event.get("id")})

        # This will raise an exception
        my_list = [1, 2, 3]
        print(my_list[5])

    except Exception:
        # Log structured message in Powertools JSON
        logger.error("Exception caught while processing event", extra={"event_id": event.get("id")})
        
        # Log full multi-line traceback using default logger
        raw_logger.error("Full stack trace:\n%s", traceback.format_exc())

        # Optionally re-raise if you want Lambda to fail
        raise
