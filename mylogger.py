import logging


class Log:
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    @staticmethod
    def init(**kwargs):
        logging.basicConfig(level=kwargs['level'],
                            format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s')

    @staticmethod
    def c(tag, msg, *args, **kwargs):
        logger = Log._getLogger(tag)
        logger.critical(msg, *args, **kwargs)

    @staticmethod
    def e(tag, msg, *args, **kwargs):
        logger = Log._getLogger(tag)
        logger.error(msg, *args, **kwargs)

    @staticmethod
    def w(tag, msg, *args, **kwargs):
        logger = Log._getLogger(tag)
        logger.debug(msg, *args, **kwargs)

    @staticmethod
    def i(tag, msg, *args, **kwargs):
        logger = Log._getLogger(tag)
        logger.info(msg, *args, **kwargs)

    @staticmethod
    def d(tag, msg, *args, **kwargs):
        logger = Log._getLogger(tag)
        logger.debug(msg, *args, **kwargs)

    @staticmethod
    def _getLogger(tag):
        # getLogger(...) returns unique object for each tag parameter
        # The tag and logger are one-to-one
        return logging.getLogger(tag)
