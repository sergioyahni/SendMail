import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
https://realpython.com/python-send-email/
'''


class Email:
    def __init__(self, email, password):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.context = ssl.create_default_context()

        self.from_email = email
        self.password = password
        self.to_email = ''
        self.message = ''

    def simple(self, to_email, subject, body):
        self.message = f'subject:{subject}\n\n{body}'
        self.to_email = to_email
        self._send()

    def send_email(self, **mail):
        print("start complex")
        # Create a multipart message and set headers
        message = MIMEMultipart()
        self.to_email = mail["to"]
        message["From"] = self.from_email
        message["To"] = mail["to"]
        if "subject" in mail:
            message["Subject"] = mail["subject"]
        if "cc" in mail:
            if isinstance(mail["cc"], list):
                message["Cc"] = mail["cc"]
        if "bcc" in mail:
            if isinstance(mail["bcc"], list):
                message["Bcc"] = mail["bcc"]

        # Add body to email
        if "body" in mail:
            message.attach(MIMEText(mail["body"], "plain"))

        if "filename" in mail:
            filename = mail["filename"]

            # Open file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
        print("attach complex")
        self.message = message.as_string()
        self._send()

    def _send(self):
        print("send mail")
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()  # Can be omitted
            server.starttls(context=self.context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, self.to_email, self.message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
