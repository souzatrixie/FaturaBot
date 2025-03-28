from smtplib import SMTP
from imaplib import IMAP4_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

class EmailHandler:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.email_user = self.config['EMAIL']['USER']
        self.email_password = self.config['EMAIL']['PASSWORD']
        self.smtp_server = self.config['EMAIL']['SMTP_SERVER']
        self.imap_server = self.config['EMAIL']['IMAP_SERVER']

    def send_email(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email_user
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with SMTP(self.smtp_server) as server:
            server.starttls()
            server.login(self.email_user, self.email_password)
            server.send_message(msg)

    def receive_emails(self):
        with IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.email_user, self.email_password)
            mail.select('inbox')
            status, messages = mail.search(None, 'ALL')
            email_ids = messages[0].split()
            emails = []

            for email_id in email_ids:
                status, msg_data = mail.fetch(email_id, '(RFC822)')
                emails.append(msg_data[0][1])

            return emails