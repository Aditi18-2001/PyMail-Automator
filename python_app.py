from email.message import EmailMessage
import ssl
import smtplib

email_sender='aditijaya2018@gmail.com'
email_password='ycvv aynp mtte bvyu'

email_receiver='aditijaya2018@gmail.com'

subject="Creating your first python mail"
body=""" Hurry! your first python mail has been sent. You did it!"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
