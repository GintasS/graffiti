import configparser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from GraffLibAPI.configuration.constants import *

config = configparser.ConfigParser()
config.read(APPSETTINGS_FILE_URI)

def create_password_recovery_email(receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "GraffLib - Password recovery"
    message["From"] = config.get("email-credentials","EmailAddress")
    message["To"] = receiver_email

    # Create the HTML version of your message    
    with open(PASSWORD_RECOVERY_TEMPLATE_FILE_URI, 'r') as f:
        html = f.read()

    # Add persons email to the template.
    html = html.replace("{email}", receiver_email)

    # Turn these into plain/html MIMEText objects
    part = MIMEText(html, "html")

    # Add HTML part to MIMEMultipart message
    message.attach(part)

    return message

def send_email(message):
    host_email_server = config.get("email-credentials","EmailServer")
    host_port = config.get("email-credentials","Port")
    host_sender_email = config.get("email-credentials","EmailAddress")
    host_email_password = config.get("email-credentials","EmailPassword")

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host_email_server, host_port, context=context) as server:
        server.login(host_sender_email, host_email_password)
        server.sendmail(
            host_sender_email, message["To"], message.as_string()
        )