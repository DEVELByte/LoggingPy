import funlog
import logging
import ex_module
from mail import send_mail


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


f_logger.f_log(logging.INFO, 'creating an instance of auxiliary_module.Auxiliary')
a = ex_module.ExClass()

f_logger.f_log(logging.INFO, 'created an instance of auxiliary_module.Auxiliary')
f_logger.f_log(logging.INFO, 'calling auxiliary_module.Auxiliary.do_something')
a.do_something()

f_logger.f_log(logging.INFO, 'finished auxiliary_module.Auxiliary.do_something')
f_logger.f_log(logging.INFO, 'calling auxiliary_module.some_function()')
ex_module.some_function()

f_logger.f_log(logging.INFO, 'done with auxiliary_module.some_function()')

send_mail('test subject with attachment', 'test mail with attachment', ['spam.log'])

send_mail('test subject without attachment', 'test mail without attachment')
