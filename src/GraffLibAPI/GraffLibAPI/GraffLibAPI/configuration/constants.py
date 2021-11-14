# Library imports.
import os
import platform
from pathlib import Path
import configparser

class UserValidation:
    USERNAME_MIN_LENGTH = 6
    USERNAME_MAX_LENGTH = 256
    USERNAME_VALIDATION_MSG = "Username must be between 6 and 256 characters."

    FISRT_NAME_MAX_LENGTH = 255
    FIRST_NAME_VALIDATION_MSG = "First name max length is 255."

    LAST_NAME_MAX_LENGTH = 255
    LAST_NAME_VALIDATION_MSG = "Last name max length is 255."

    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 128
    PASSWORD_VALIDATION_MSG = "Password must be between 8 and 128 characters."  

    PASSWORD_BINARY_FORM_MAX_LENGTH = 60
    PASSWORD_BINARY_FORM_VALIDATION_MSG = "Password bytes max count is 60."
    
    EMAIL_MIN_LENGTH = 3
    EMAIL_MAX_LENGTH = 320
    EMAIL_VALIDATION_MSG = "Email address must be a valid one."     

class PasswordResetValidation:
    # Python secure library will create on average 1.3 characters per single byte.
    # This equals to 41.6 characters on average.
    PASSWORD_RESET_TOKEN_MIN_LENGTH = 38 
    PASSWORD_RESET_TOKEN_MAX_LENGTH = 44
    PASSWORD_RESET_TOKEN_VALIDATION_MSG = "Token must be between 32 and 48 characters."

class ImageValidation:
    # Image
    # Same as PASSWORD_RESET_TOKEN, Python secure library will create a hashed name for the name.
    IMAGE_UNIQUE_NAME_MIN_LENGTH = 38
    IMAGE_UNIQUE_NAME_MAX_LENGTH = 44
    IMAGE_UNIQUE_NAME_VALIDATION_MSG = "Image unique name must be between 41 and 42 characters."

    USER_PROVIDED_IMAGE_NAME_MIN_LENGTH = 3
    USER_PROVIDED_IMAGE_NAME_MAX_LENGTH = 60
    USER_PROVIDED_IMAGE_NAME_VALIDATION_MSG = "User provided image name must be between 50 and 60 characters."

    IMAGE_EXTENSION_MIN_LENGTH = 3
    IMAGE_EXTENSION_MAX_LENGTH = 5
    IMAGE_EXTENSION_VALIDATION_MSG = "Image extension length should be between 3 and 5 characters."

    IMAGE_DESCRIPTION_MIN_LENGTH = 3
    IMAGE_DESCRIPTION_MAX_LENGTH = 180
    IMAGE_DESCRIPTION_VALIDATION_MSG = "Image description must be between 20 and 180 characters."

    IMAGE_GRAFFITI_OBJECT_MIN_LENGTH = 3
    IMAGE_GRAFFITI_OBJECT_MAX_LENGTH = 50
    IMAGE_GRAFFITI_OBJECT_VALIDATION_MSG = "Graffiti object must be between 3 and 50 characters."

    IMAGE_ORIGINAL_NAME_MIN_LENGTH = 1
    IMAGE_ORIGINAL_NAME_MAX_LENGTH = 100
    IMAGE_ORIGINAL_NAME_VALIDATION_MSG = "Image original name must be between 1 and 100 characters."

    IMAGE_ALLOWED_EXTENSIONS = [
      "jpeg", 
      "png"
    ]

    HTTP_REQUEST_MIME_TYPES = [
      "image/jpeg",
      "image/png"
    ]

class MarkerValidation:
    MARKER_ID_MIN_LENGTH = 41  
    MARKER_ID_MAX_LENGTH = 42
    MARKER_ID_VALIDATION_MSG = "Marker ID must be between 41 and 42 characters."


class LocationValidation:
    COUNTRY_NAME_MIN_LENGTH = 4
    COUNTRY_NAME_MAX_LENGTH = 90
    COUNTRY_NAME_VALIDATION_MSG = "Country must be between 4 and 90 characters long."

    CITY_NAME_MIN_LENGTH = 4
    CITY_NAME_MAX_LENGTH = 28
    CITY_NAME_VALIDATION_MSG = "City must be between 4 and 28 characters long."

    STREET_ADDRESS_MIN_LENGTH = 50
    STREET_ADDRESS_MAX_LENGTH = 100
    STREET_ADDRESS_VALIDATION_MSG = "Address must be between 50 and 100 characters long."

    COORDINATES_LIST_MIN_ELEMENTS = 2
    COORDINATES_LIST_MAX_ELEMENTS = 2
    COORDINATES_VALIDATION_MSG = "Coordinates array must contain two elements, latitude and longitude."

    NEW_MARKER_MIN_DISTANCE_BETWEEN_EXISTING_MARKER = 0.1

class MiscValidation:
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    URL_SCHEME_HTTP = "http"
    URL_SCHEME_HTTPS = "https"

# OS related path constants.

class Directory:
    WORKING_DIRECTORY = str(Path.cwd())
    CONFIGURATION_DIRECTORY = "configuration"
    TEMPLATES_DIRECTORY = "templates"
    EMAIL_TEMPLATES_DIRECTORY = "email-templates"
    GRAFFLIB_ROOT_DIRECTORY = "GraffLibAPI"

class FilePath:
    APPSETTINGS_FILE = "appsettings.ini"
    APPSETTINGS_FILE_URI = os.path.join(Directory.WORKING_DIRECTORY, Directory.GRAFFLIB_ROOT_DIRECTORY, Directory.CONFIGURATION_DIRECTORY, APPSETTINGS_FILE)

    PASSWORD_RECOVERY_TEMPLATE_FILE = "password-recovery-template.html"
    PASSWORD_RECOVERY_TEMPLATE_FILE_URI = os.path.join(Directory.WORKING_DIRECTORY, Directory.GRAFFLIB_ROOT_DIRECTORY, Directory.TEMPLATES_DIRECTORY, Directory.EMAIL_TEMPLATES_DIRECTORY, PASSWORD_RECOVERY_TEMPLATE_FILE)

    DATABASE_FILE = "dbsettings.ini"
    DATABASE_FILE_URI = os.path.join(Directory.WORKING_DIRECTORY, Directory.GRAFFLIB_ROOT_DIRECTORY, Directory.CONFIGURATION_DIRECTORY, DATABASE_FILE)

    ENVIRONMENT_FILE = "environment.ini"
    ENVIRONMENT_FILE_URI = os.path.join(Directory.WORKING_DIRECTORY, Directory.GRAFFLIB_ROOT_DIRECTORY, Directory.CONFIGURATION_DIRECTORY, ENVIRONMENT_FILE)


class Environment:
    config = configparser.ConfigParser()
    config.read(FilePath.ENVIRONMENT_FILE_URI)   
    CURRENT_ENVIRONMENT_NAME = config.get("environment", "CURRENT_ENVIRONMENT_NAME")

class Database():   
    POSTGRES_DATABASE_URI = "postgresql+psycopg2://{db-user}:{db-password}@{db-url}:{db-url-port}/{db-name}"

    def get_replaced_databse_uri():
        postgres_url = Database.POSTGRES_DATABASE_URI
        config_name = None

        if Environment.CURRENT_ENVIRONMENT_NAME == "DEV":
            config_name = "db-credentials-dev"
        if Environment.CURRENT_ENVIRONMENT_NAME == "PROD":
            config_name = "db-credentials-prod"

        config = configparser.ConfigParser()
        config.read(FilePath.DATABASE_FILE_URI)

        db_user = config.get(config_name, "POSTGRES_DB_USER_NAME")
        db_password = config.get(config_name, "POSTGRES_DB_PASSWORD")
        db_url = config.get(config_name, "POSTGRES_DB_URL")
        db_url_port = config.get(config_name, "POSTGRES_DB_URL_PORT")
        db_name = config.get(config_name, "POSTGRES_DB_NAME")

        return postgres_url.replace("{db-user}", db_user) \
            .replace("{db-password}", db_password) \
            .replace("{db-url}", db_url) \
            .replace("{db-url-port}", db_url_port) \
            .replace("{db-name}", db_name) \

class Application:
    APP_URL = None

    config = configparser.ConfigParser()
    config.read(FilePath.APPSETTINGS_FILE_URI)
    
    if Environment.CURRENT_ENVIRONMENT_NAME == "DEV":
        APP_URL = config.get("app", "DEV_URL")
    if Environment.CURRENT_ENVIRONMENT_NAME == "PROD":
        APP_URL = config.get("app", "PROD_URL")