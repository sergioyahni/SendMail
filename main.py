from mail import Email

sender_mail = "YOU@GMAIL.COM"
password = "YOUR_PASSWORD"

email = Email(sender_mail, password)

email.send_email(to="RECIPIENT",
                 cc="CC",
                 bcc="BCC",
                 subject="SUBJECT",
                 body="YOUR MESSAGE",
                 filename="FILE_TO_ATTACH")
