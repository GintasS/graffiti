import configparser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.configuration.email_credentials import EmailCredentials

config = configparser.ConfigParser()
config.read(FilePath.APPSETTINGS_FILE_URI)

def create_password_reset_url(reset_token : str) -> str:
    base_url = "{app_url}/v1/password?token={reset_token}"
    base_url = base_url.replace("{reset_token}", reset_token)
    base_url = base_url.replace("{app_url}", Application.APP_URL)

    return base_url

# TODO: [EMAIL SENDING] [PROD] Try use 3rd party service for sending emails, because gmail doesn't work in AWS.

def create_password_recovery_email(receiver_email : str, password_reset_link : str) -> None:
    message = MIMEMultipart("alternative")
    message["Subject"] = u"GraffLib - Password recovery"
    message["From"] = config.get("email-credentials","EmailAddress")
    message["To"] = receiver_email

    # Create the HTML version of your message    
    with open(FilePath.PASSWORD_RECOVERY_TEMPLATE_FILE_URI, 'r') as f:
        html = f.read()

    # Add persons email to the template.
    text = """\
    Hi,
    How are you?
    Password recovery link is here: {password-recovery-link}
    """

    # Replace all placeholders in the email template.
    text = text.replace("{password-reset-link}", password_reset_link)

    html = html.replace("{email}", receiver_email)
    html = html.replace("{password-reset-link}", password_reset_link)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain", "utf-8")
    part2 = MIMEText(html, "html", "utf-8")

    # Add HTML part to MIMEMultipart message
    message.attach(part1)
    message.attach(part2)

    return message

def get_email_credentials() -> EmailCredentials:
    host_email_server = config.get("email-credentials","EmailServer")
    host_port = config.get("email-credentials","Port")
    host_sender_email = config.get("email-credentials","EmailAddress")
    host_email_password = config.get("email-credentials","EmailPassword")
    
    return EmailCredentials(host_email_server, host_port, host_sender_email, host_email_password)

def send_email(message : MIMEMultipart, email_credentials : EmailCredentials) -> None:
    # Get credentials.
    host_email_server = email_credentials.host_email_server
    host_port = email_credentials.host_port
    host_sender_email = email_credentials.host_sender_email
    host_email_password = email_credentials.host_email_password

    # Create secure connection with server and send email.
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host_email_server, host_port, context=context) as server:
        server.login(host_sender_email, host_email_password)
        server.sendmail(
            host_sender_email, message["To"], message.as_string().encode('ascii')
        )