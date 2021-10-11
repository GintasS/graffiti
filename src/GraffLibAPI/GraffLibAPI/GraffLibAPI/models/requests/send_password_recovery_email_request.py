# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.configuration.constants import *

class SendPasswordRecoveryEmailRequest():
    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<SendPasswordRecoveryEmailRequest(name={self.user_name!r})>'.format(self=self)

# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.
class SendPasswordRecoveryEmailRequestSchema(Schema):
    email = fields.Email(min=EMAIL_MIN_LENGTH, max=EMAIL_MAX_LENGTH, error=EMAIL_VALIDATION_MSG)

    @post_load
    def make_send_password_recovery_email_request(self, data, **kwargs):
        return SendPasswordRecoveryEmailRequest(**data)

