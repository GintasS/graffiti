import pytest
import GraffLibAPI.utils.email_sender_helper as EmailSenderClass
import configparser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.configuration.email_credentials import EmailCredentials

def test_create_password_reset_url():
    test_base_url = "{app_url}/v1/password?token=123"
    base_url = test_base_url.replace("{app_url}", Application.APP_URL)
    result_url = EmailSenderClass.create_password_reset_url("123")
    assert result_url == test_base_url

def test_get_email_credentials():
    result_EmailCredentials = EmailSenderClass.get_email_credentials()
    test_host_email_server = config.get("email-credentials","EmailServer")
    test_host_port = config.get("email-credentials","Port")
    test_host_sender_email = config.get("email-credentials","EmailAddress")
    test_host_email_password = config.get("email-credentials","EmailPassword")
    assert result_EmailCredentials.host_email_server == test_host_email_server and\
           result_EmailCredentials.host_port == test_host_port and\
           result_EmailCredentials.host_sender_email == test_host_sender_email and\
           result_EmailCredentials.host_email_password == test_host_email_password
