import sys
import logging
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "cbc.log"

class CBCLogger(object):
    logger = None

    def __init__():
        pass

    @classmethod
    def get_console_handler(cls):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    @classmethod
    def get_file_handler(cls):
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler

    @classmethod
    def get_logger(cls, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG) # better to have too much log than not enough
        logger.addHandler(cls.get_console_handler())
        logger.addHandler(cls.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger

    @classmethod
    def debug(cls, log_message):
        if cls.logger is None:
            cls.logger = cls.get_logger("CBC")
        cls.logger.debug(log_message)
