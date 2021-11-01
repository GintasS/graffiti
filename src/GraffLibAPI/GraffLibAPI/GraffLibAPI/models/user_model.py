import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.role_type import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *

class UserModel():
    def __init__(self, user_name, first_name, last_name, email, password, role):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.user_name!r})>'.format(self=self)

# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# Other: https://marshmallow.readthedocs.io/en/stable/quickstart.html
# Validators: https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html
class UserModelSchema(Schema):
    user_name = fields.Str(required=True, validate=validate.Length(UserValidation.USERNAME_MIN_LENGTH, UserValidation.USERNAME_MAX_LENGTH, error=UserValidation.USERNAME_VALIDATION_MSG))
    first_name = fields.Str(required=True, validate=validate.Length(max=UserValidation.FISRT_NAME_MAX_LENGTH, error=UserValidation.FIRST_NAME_VALIDATION_MSG))
    last_name = fields.Str(required=True, validate=validate.Length(max=UserValidation.LAST_NAME_MAX_LENGTH, error=UserValidation.LAST_NAME_VALIDATION_MSG))
    email = fields.Email(required=True, validate=validate.Length(UserValidation.EMAIL_MIN_LENGTH, UserValidation.EMAIL_MAX_LENGTH, error=UserValidation.EMAIL_VALIDATION_MSG))
    password = fields.Str(required=True, validate=validate.Length(UserValidation.PASSWORD_MIN_LENGTH, UserValidation.PASSWORD_MAX_LENGTH, error=UserValidation.PASSWORD_VALIDATION_MSG))
    role = EnumField(RoleType, required=True)
    created_at = fields.DateTime(format=MiscValidation.DATE_FORMAT)
