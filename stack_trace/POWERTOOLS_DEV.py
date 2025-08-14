import os
from aws_lambda_powertools import Logger

os.environ["POWERTOOLS_DEV"] = "1"  # enable developer mode

logger = Logger(service="payment-service")

def lambda_handler(event, context):
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except Exception:
        logger.exception("Processing failed")
