# SendMail
Use a GMAIL account to send mails. 

1. Import and initiate the Email class

**email = Email(sender_mail, password)**

2a. Send mail using the *simple* method - all arguments are mandatory: 

**email.simple("recipient", "mail subjec", "the body of your message")**

2b. Send mail using the *send_mail* method. Key "to" is a mandatory, all other keys are optionals. 

**email.send_email(to="RECIPIENT", cc="CC", bcc="BCC", subject="SUBJECT", body="YOUR MESSAGE", filename="PATH_TO_FILE")**

