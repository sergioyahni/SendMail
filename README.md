# SendMail
Use a GMAIL account to send mails. 
import and initiate the Email class

**email = Email(sender_mail, password)**

Then send mail using the send_mail method. Key "to" is a mandatory, all other keys are optionals. 


**email.send_email(to="RECIPIENT", cc="CC", bcc="BCC", subject="SUBJECT", body="YOUR MESSAGE", filename="FILE_TO_ATTACH")**

