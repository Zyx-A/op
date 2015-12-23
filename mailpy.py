#!/usr/bin/python
import sys
import smtplib
from email.Message import Message

def send(subject, content, to, ssl=0):
    smtp = 'smtp.qq.com'
    mail_addr = 'romi@qq.com'
    password = 'ndfewwgeewg2323tf8'
    loginuser = mail_addr

    msg = Message()
    msg['From'] = mail_addr
    msg['Subject'] = subject
    if isinstance(to,str):
        msg['To'] = to
    else:
        msg['To'] = ', '.join(to)

    if ssl == 1:
        sm = smtplib.SMTP_SSL()
    else:
        sm = smtplib.SMTP()
    sm.connect(smtp)
    sm.ehlo()
    sm.login(loginuser,password)
    sm.sendmail(mail_addr,to,msg.as_string()+content)
    sm.close()

if __name__ == '__main__':
    content = sys.stdin.read()
    if sys.argv[1] == '-s':
        subject = sys.argv[2]
        to = sys.argv[3].split(';')
    else:
        subject = 'No Subject'
        to = sys.argv[1].split(';')
    send(subject, content, to)


