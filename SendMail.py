import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import config
'''
To send messages with a gmail smtp you may want to use 
google app password (if your gmail account uses 2-Step-Verification)
or set your gmail account to work with less secure apps (In this case 
gmail may not send binary attachements). 

Google security page: https://myaccount.google.com/u/1/security

Read more: https://support.google.com/accounts/answer/185833?hl=en
'''


def send_email():
    # Set up the MIME
    msg = MIMEMultipart()
    msg['from'] = config.email
    msg['to'] = 'sergioyahni@gmail.com'
    msg['subject'] = 'Test: Send attachement'
    
    # Create and attach the message
    body = 'Test sending attachements with gmail from an external app'
    msg.attach(MIMEText(body, 'plain'))
    filename = 'reservation.pdf'
    attachement = open('reservation.pdf', 'rb')
    
    # setup the playload
    p = MIMEBase('application', 'octete-stream')
    p.set_payload((attachement).read())
    encoders.encode_base64(p)
    p.add_header(f'Content-Disposition', 'attachment', filename=filename)
    msg.attach(p)
    
    # Create a server and send the email 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(config.email, config.password)
    text = msg.as_string()
    s.sendmail(config.email, 'sergioyahni@gmail.com', text)
    
    # quit the mail server
    s.quit()


if __name__ == '__main__':
    send_email()
