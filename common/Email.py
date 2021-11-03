# -*- coding: utf-8 -*-
# 163邮箱，需要开启 IMAP/SMTP服务


import time
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from common import get_Config   # 加上文件路径，才能正确调用


def send_email(text):
    today = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    sender, receiver, smtpserver, username, password = get_Config.get_email_Conf()
    # subject为邮件主题 text为邮件正文
    subject = "EPSP自动化测试结果通知 {}".format(today)
    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = "".join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    #smtp.ehlo()
    #smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
