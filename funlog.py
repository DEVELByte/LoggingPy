import logging
import config


# ------------------------------------------------------------------------
__author__ = "NareN"
__copyright__ = "Copyright 2015 The develByte Project"
__credits__ = ["Narendra Kumar"]
__license__ = " "
__version__ = "0.1"
__maintainer__ = "NareN"
__email__ = "naren@develbyte.in"
# ------------------------------------------------------------------------


class FunLogger:
    __location = 'None'
    __logfile = 'None'
    __level = 'None'
    __format = 'None'

    def __init__(self, location, filename):

        self.__location = location
        self.__logfile = filename
        self.__level = config.log_level
        self.__format = config.log_format

        self.logger = logging.getLogger(location)
        self.logger.setLevel(self.__level)

        fh = logging.FileHandler(self.__logfile)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        formatter = logging.Formatter(self.__format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def f_log(self, log_type, message):

        if log_type == logging.DEBUG:
            self.logger.debug(str(message))

        elif log_type == logging.INFO:
            self.logger.info(str(message))

        elif log_type == logging.WARNING:
            self.logger.warning(str(message))

        elif log_type == logging.ERROR:
            self.logger.error(str(message))

        elif log_type == logging.CRITICAL:
            self.logger.critical(str(message))
