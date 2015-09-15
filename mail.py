import smtplib
import logging
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import MailConfig
import funlog


# ------------------------------------------------------------------------
__author__ = "NareN"
__copyright__ = "Copyright 2015 The develByte Project"
__credits__ = ["Narendra Kumar"]
__license__ = " "
__version__ = "0.1"
__maintainer__ = "NareN"
__email__ = "naren@develbyte.in"
# -------------------------------------------------------------------------

f_logger = funlog.FunLogger('mail', 'spam.log')


def send_mail(subject, msg, files=[]):
    msg = get_mime_msg(subject, msg, files)
    server = smtplib.SMTP(MailConfig['mailserver'])

    try:
        server.ehlo()
        server.starttls()
        server.ehlo()

    except Exception as err:
        f_logger.f_log(logging.ERROR, "Connection to server has failed")
        f_logger.f_log(logging.ERROR, err)

    try:
        server.login(MailConfig['from'], MailConfig['passwd'])

    except Exception as err:
        f_logger.f_log(logging.ERROR, "Login to mail has failed")
        f_logger.f_log(logging.ERROR, err)

    try:
        server.sendmail(MailConfig['from'], MailConfig['to'], msg.as_string())

    except Exception as err:
        f_logger.f_log(logging.ERROR, "Mail sending has failed")
        f_logger.f_log(logging.ERROR, err)

    server.quit()


def get_mime_msg(subject, content, files):
    msg = MIMEMultipart("Query Result")
    msg['subject'] = subject
    msg['to'] = MailConfig['to']
    if len(files) > 0:
        msg.attach(MIMEText(content, 'plain'))
        for f in files or []:
            with open(f, "rb") as fil:
                msg.attach(MIMEApplication(fil.read(), Content_Disposition='attachment; filename="%s"' % basename(f),
                                           Name=basename(f)
                                           ))

    return msg
