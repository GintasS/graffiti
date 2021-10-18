import os
import platform

# Validation

USERNAME_MIN_LENGTH = 6
USERNAME_MAX_LENGTH = 256

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

EMAIL_MIN_LENGTH = 3
EMAIL_MAX_LENGTH = 320

USERNAME_VALIDATION_MSG = "Username must be between 6 and 256 characters."
EMAIL_VALIDATION_MSG = "Email address must be a valid one."
PASSWORD_VALIDATION_MSG = "Password must be between 8 and 128 characters."

# Python secure library will create on average 1.3 characters per single byte.
# This equals to 41.6 characters on average.
PASSWORD_RESET_TOKEN_MIN_LENGTH = 41  
PASSWORD_RESET_TOKEN_MAX_LENGTH = 42

PASSWORD_RESET_TOKEN_VALIDATION_MSG = "Token must be between 32 and 48 characters."

# Image
# Same as PASSWORD_RESET_TOKEN, Python secure library will create a hashed name for the name.
IMAGE_UNIQUE_NAME_MIN_LENGTH = 41  
IMAGE_UNIQUE_NAME_MAX_LENGTH = 42

USER_PROVIDED_IMAGE_NAME_MIN_LENGTH = 50
USER_PROVIDED_IMAGE_NAME_MAX_LENGTH = 60

IMAGE_EXTENSION_MIN_LENGTH = 3
IMAGE_EXTENSION_MAX_LENGTH = 5

IMAGE_EXTENSION_VALIDATION_MSG = "Image Extension length should be between 3 and 5."

IMAGE_DESCRIPTION_MIN_LENGTH = 0
IMAGE_DESCRIPTION_MAX_LENGTH = 180

IMAGE_UNIQUE_URL_MAX_LENGTH = 62

# General
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"





# Database
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:admin@localhost:5432/grafflib"


# OS related path constants.
if platform.system().lower() == "windows" or platform.system().lower() == "linux":
    APPSETTINGS_FILE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/configuration/appsettings.ini"
    APPSETTINGS_FILE_URI = os.path.abspath(APPSETTINGS_FILE_RELATIVE_PATH)

    PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/templates/email-templates/password-recovery-template.html"
    PASSWORD_RECOVERY_TEMPLATE_FILE_URI = os.path.abspath(PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH)


else:
    APPSETTINGS_FILE_RELATIVE_PATH = "src/GraffLibAPI/GraffLibAPI/configuration/appsettings.ini"
    APPSETTINGS_FILE_URI = os.path.abspath(APPSETTINGS_FILE_RELATIVE_PATH)

    PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH = "src/GraffLibAPI/GraffLibAPI/templates/email-templates/password-recovery-template.html"
    PASSWORD_RECOVERY_TEMPLATE_FILE_URI = os.path.abspath(PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH)
