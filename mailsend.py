#!/usr/bin/python
import smtplib
from email.Message import Message

def send(subject,content,to,ssl=0):
        smtp = 'smtp.qq.com'
        mail_addr = 'sb8@qq.com'
        password = 'pwd'
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
