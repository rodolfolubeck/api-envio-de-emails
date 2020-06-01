import smtplib
from .secrets import myemail, pw
from datetime import date
from email.message import EmailMessage


class Contact:

    def __init__(self, identifier, email, name, send_date):
        self.identifier = identifier
        self.email = email
        self.name = name
        self.send_date = send_date

    def send_email(self, contact):

        email_address = myemail
        email_password = pw

        msg = EmailMessage()
        msg['subject'] = 'E-mail contact from python!'
        msg['From'] = email_address
        msg['To'] = contact.email
        msg.set_content('This is the e-mail content text')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)

            smtp.send_message(msg)