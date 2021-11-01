
import logging
from log_main import FileLogger
logger = FileLogger(__name__).get_logger()


def out_b():
    logger.info("hello, is b.py| out_b() .....")