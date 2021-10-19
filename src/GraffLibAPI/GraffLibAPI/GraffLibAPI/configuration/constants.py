import os
import platform

# Validation
# UserModel
USERNAME_MIN_LENGTH = 6
USERNAME_MAX_LENGTH = 256

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

EMAIL_MIN_LENGTH = 3
EMAIL_MAX_LENGTH = 320

USERNAME_VALIDATION_MSG = "Username must be between 6 and 256 characters."
EMAIL_VALIDATION_MSG = "Email address must be a valid one."
PASSWORD_VALIDATION_MSG = "Password must be between 8 and 128 characters."

# UpdateUnauthenticatedPasswordRequest

# Python secure library will create on average 1.3 characters per single byte.
# This equals to 41.6 characters on average.
PASSWORD_RESET_TOKEN_MIN_LENGTH = 32  
PASSWORD_RESET_TOKEN_MAX_LENGTH = 48

PASSWORD_RESET_TOKEN_VALIDATION_MSG = "Token must be between 32 and 48 characters."

# Database constants
if platform.system().lower() == "windows" or platform.system().lower() == "linux":
    DATABASE_FILE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/database/main-db.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(DATABASE_FILE_RELATIVE_PATH)

    APPSETTINGS_FILE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/configuration/appsettings.ini"
    APPSETTINGS_FILE_URI = os.path.abspath(APPSETTINGS_FILE_RELATIVE_PATH)

    PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/templates/email-templates/password-recovery-template.html"
    PASSWORD_RECOVERY_TEMPLATE_FILE_URI = os.path.abspath(PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH)


else:
    DATABASE_FILE_RELATIVE_PATH = "src/GraffLibAPI/GraffLibAPI/GraffLibAPI/database/main-db.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(DATABASE_FILE_RELATIVE_PATH)

    APPSETTINGS_FILE_RELATIVE_PATH = "src/GraffLibAPI/GraffLibAPI/configuration/appsettings.ini"
    APPSETTINGS_FILE_URI = os.path.abspath(APPSETTINGS_FILE_RELATIVE_PATH)

    PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH = "src/GraffLibAPI/GraffLibAPI/templates/email-templates/password-recovery-template.html"
    PASSWORD_RECOVERY_TEMPLATE_FILE_URI = os.path.abspath(PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH)
