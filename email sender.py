# go over to chrome 
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'successdavidpraise99@gmail.com'
email_password = 'rtjl rwhj eqds uuqn'

email_receiver = 'yixekev572@avashost.com'

subject = "im testing sme pooiomething sorry"

body = """ 
when you see this text or call me 
"""
#to do this one need to undersend ssl and smtlip

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

# send the email

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# this project helps in later projects. 
