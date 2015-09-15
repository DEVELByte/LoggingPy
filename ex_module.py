import logging
import funlog

# ------------------------------------------------------------------------
__author__ = "NareN"
__copyright__ = "Copyright 2015 The develByte Project"
__credits__ = ["Narendra Kumar"]
__license__ = " "
__version__ = "0.1"
__maintainer__ = "NareN"
__email__ = "naren@develbyte.in"
# ------------------------------------------------------------------------
f_logger = funlog.FunLogger(__name__, 'spam.log')


class ExClass:
    def __init__(self):
        f_logger.f_log(logging.INFO, 'spam_application.auxiliary.Auxiliary')
        f_logger.f_log(logging.INFO, 'creating an instance of Auxiliary')

    @staticmethod
    def do_something():
        f_logger.f_log(logging.INFO, 'doing something')
        a = 1 + 1
        f_logger.f_log(logging.INFO, 'done doing something')


def some_function():
    f_logger.f_log(logging.INFO, 'received a call to "some_function"')
