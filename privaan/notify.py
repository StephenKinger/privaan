import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import *

def notify(content) :
    # The actual mail send
    msg = MIMEMultipart('alternative')
    if content.find('GRANTED') != -1:
        msg['Subject'] = "Granted Access Report"
    else:
        msg['Subject'] = "Log Report"
    part = MIMEText(content.encode('utf-8'), 'html')
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()