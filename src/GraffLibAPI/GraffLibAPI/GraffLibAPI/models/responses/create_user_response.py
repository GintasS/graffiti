import json

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema
from GraffLibAPI.configuration.constants import *

class CreateUserResponse():
    def __init__(self, user_id, user_name, email, created_at):
       self.user_id = user_id
       self.user_name = user_name
       self.email = email
       self.created_at = created_at

# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.

class CreateUserResponseSchema(Schema):
    user_id = fields.Int(required=True)
    first_name = fields.Str(required=True, validate=validate.Length(max=UserValidation.FISRT_NAME_MAX_LENGTH, error=UserValidation.FIRST_NAME_VALIDATION_MSG))
    last_name = fields.Str(required=True, validate=validate.Length(max=UserValidation.LAST_NAME_MAX_LENGTH, error=UserValidation.LAST_NAME_VALIDATION_MSG))
    email = fields.Email(required=True, validate=validate.Length(UserValidation.EMAIL_MIN_LENGTH, UserValidation.EMAIL_MAX_LENGTH, error=UserValidation.EMAIL_VALIDATION_MSG))
    created_at = fields.DateTime(required=True, format=MiscValidation.DATE_FORMAT)