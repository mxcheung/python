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



import traceback
import sys
from aws_lambda_powertools import Logger

logger = Logger(service="payment-service")

def lambda_handler(event, context):
    try:
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise ValueError("Higher-level error") from e
    except Exception:
        exc_type, exc_value, exc_tb = sys.exc_info()
        logger.error("Full chained traceback:\n%s",
                     "".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
