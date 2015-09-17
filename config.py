import logging
from datetime import date

# ------------------------------------------------------------------------
__author__ = "NareN"
__copyright__ = "Copyright 2015 The develByte Project"
__credits__ = ["Narendra Kumar"]
__license__ = " "
__version__ = "0.1"
__maintainer__ = "NareN"
__email__ = "naren@develbyte.in"
# ------------------------------------------------------------------------


# ----------------------------------------------------------------
# logging configs
# ----------------------------------------------------------------
log_file = 'test_log_' + date + '.log'
log_level = logging.DEBUG
log_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

# ----------------------------------------------------------------
# mail configs
# ----------------------------------------------------------------
MailConfig = {
    'from': 'naren@develbyte.in',
    'to': 'naren@develbyte.in',
    'host': 'smtp.gmail.com:***PORT NUMBER GOES HERE****',
    'passwd': '***PASSWORD GOES HERE****',
    'mailserver': 'smtp.gmail.com:***PORT NUMBER GOES HERE****'
}