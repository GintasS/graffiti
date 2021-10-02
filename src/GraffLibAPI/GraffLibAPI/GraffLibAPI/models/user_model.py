import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums import RoleType
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
    user_name = fields.Str(validate=validate.Length(min=USERNAME_MIN_LENGTH, max=USERNAME_MAX_LENGTH, error=USERNAME_VALIDATION_MSG))
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email(min=EMAIL_MIN_LENGTH, max=EMAIL_MAX_LENGTH, error=EMAIL_VALIDATION_MSG)
    password = fields.Str(validate=validate.Length(min=PASSWORD_MIN_LENGTH, max=PASSWORD_MAX_LENGTH, error=PASSWORD_VALIDATION_MSG))
    role = EnumField(RoleType.RoleType)
    created_at = fields.Date()
