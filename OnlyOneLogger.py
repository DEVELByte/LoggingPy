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

# OnlyOneLogger follows Singleton Design Pattern
# Singleton Design Pattern : In software engineering, the singleton pattern
#           is a design pattern that restricts the instantiation of a class
#           to one object. This is useful when exactly one object is needed
#           to coordinate actions across the system.
# ref: https://en.wikipedia.org/wiki/Singleton_pattern
# ------------------------------------------------------------------------


class OnlyOneLogger:

    class __FunLogger:
        location = 'None'
        __logfile = 'None'
        __level = 'None'
        __format = 'None'

        def __init__(self, location):

            self.location = location
            self.__logfile = config.log_file
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

        def __f_log__(self, log_type, message):

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

    instance = None

    def __init__(self, location, log_type, message):
        if not OnlyOneLogger.instance:
            OnlyOneLogger.instance = OnlyOneLogger.__FunLogger(location)
            OnlyOneLogger.__FunLogger(location).__f_log__(log_type, message)
        else:
            OnlyOneLogger.instance.location = location
            OnlyOneLogger.instance.__f_log__(log_type, message)
