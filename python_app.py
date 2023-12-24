from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
import ssl
import smtplib

email_sender='aditijaya2018@gmail.com'
email_password='qmzx oukn oehy vkbb'

email_receiver='aditijaya2018@gmail.com'

subject="Creating your first python mail"
body=""" Hurry! your first python mail has been sent. You did it!"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

# Attach a file
file_path = 'D:/Users/hp/Downloads/voters ID.pdf'  # Replace with the actual path to your file
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(open(file_path, "rb").read())
encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", f"attachment; filename={file_path}")
em.add_attachment(attachment)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())