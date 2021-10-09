import os

# Validation limits
# UserModel
USERNAME_MIN_LENGTH = 6
USERNAME_MAX_LENGTH = 256

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128

EMAIL_MIN_LENGTH = 3
EMAIL_MAX_LENGTH = 320

# Validation error messages
# UserModel
USERNAME_VALIDATION_MSG = "Username must be between 6 and 256 characters."
EMAIL_VALIDATION_MSG = "Email address must be a valid one."
PASSWORD_VALIDATION_MSG = "Password must be between 8 and 128 characters."

# Database constants
DATABASE_FILE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/database/main-db.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(DATABASE_FILE_RELATIVE_PATH)

APPSETTINGS_FILE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/configuration/appsettings.ini"
APPSETTINGS_FILE_URI = os.path.abspath(APPSETTINGS_FILE_RELATIVE_PATH)

PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH = "../GraffLibAPI/GraffLibAPI/static/content/email-templates/password-recovery-template.html"
PASSWORD_RECOVERY_TEMPLATE_FILE_URI  = os.path.abspath(PASSWORD_RECOVERY_TEMPLATE_RELATIVE_PATH)