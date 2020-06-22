import logging

CRITICAL = logging.CRITICAL
FATAL = CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG


class Log:
    @staticmethod
    def init(**kwargs):
        logging.basicConfig(level=kwargs['level'], format=kwargs['format'])

    @staticmethod
    def _getlogger(tag):
        return logging.getLogger(tag)

    @staticmethod
    def c(tag, msg, *args, **kwargs):
        logger = Log._getlogger(tag)
        logger.critical(msg, *args, **kwargs)

    @staticmethod
    def e(tag, msg, *args, **kwargs):
        logger = Log._getlogger(tag)
        logger.error(msg, *args, **kwargs)

    @staticmethod
    def w(tag, msg, *args, **kwargs):
        logger = Log._getlogger(tag)
        logger.debug(msg, *args, **kwargs)

    @staticmethod
    def i(tag, msg, *args, **kwargs):
        logger = Log._getlogger(tag)
        logger.info(msg, *args, **kwargs)

    @staticmethod
    def d(tag, msg, *args, **kwargs):
        logger = Log._getlogger(tag)
        logger.debug(msg, *args, **kwargs)

