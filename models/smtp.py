import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import render_template


class SMTP:

    def __init__(self, send_gmail):
        self.msg = MIMEMultipart("alternative")
        self.password = os.environ.get("EMAIL_PASSWORD")
        self.sender = os.environ.get("EMAIL")
        self.receiver = send_gmail
        self.msg['From'] = formataddr(('no-reply', os.environ.get("EMAIL")))
        self.msg['To'] = send_gmail

    def send_emai(self, id_, zk, sm):
        try:
            self.msg['Subject'] = "Заказ"
            email_content = render_template('smtp.html', id=id_, jso=zk, sm=sm)
            email_content = MIMEText(email_content, "html", "utf-8")
            self.msg.attach(email_content)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.mail.ru", 465, context=context) as server:
                server.login(self.sender, self.password)
                server.sendmail(
                    self.msg['From'], self.msg['To'], self.msg.as_string()
                )
            return True
        except Exception as e:
            print("Cбой (send_email)" + '\n' + str(e))
            return False
