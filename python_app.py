from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
import urllib.parse  # Import the urllib.parse module

email_sender = 'aditijaya2018@gmail.com'
email_password = 'mpyj igom gsoc zqck'
email_receiver = 'aditijaya2018@gmail.com'

subject = "Creating your first python mail"
body = """Hurry! your first python mail has been sent. You did it!"""

# Create a multipart email message
em = MIMEMultipart()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

# Attach the text body
em.attach(MIMEText(body, 'plain'))

# Adding a file attachment
file_path = 'D:/Users/hp/Downloads/voters ID.pdf'  # Update the file path
file_path_encoded = urllib.parse.quote(file_path)  # Encode the file path

attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(open(file_path, 'rb').read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', f'attachment; filename="{file_path_encoded}"')  # Use the encoded file path
em.attach(attachment)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
