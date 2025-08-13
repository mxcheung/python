import traceback
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # IndexError
    except Exception:
        exc_type, exc_value, exc_tb = sys.exc_info()
        formatted_trace = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        logger.error("Pretty Stack Trace:\n%s", formatted_trace)
