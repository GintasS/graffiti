import datetime as dt
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.configuration.constants import *

class UpdateUnauthenticatedUserPasswordRequest():
    def __init__(self, token, new_password):
       self.token = token
       self.new_password = new_password

    def __repr__(self):
        return '<UpdateUnauthenticatedUserPasswordRequest(name={self.user_id!r})>'.format(self=self)

class UpdateUnauthenticatedUserPasswordRequestSchema(Schema):
    token = fields.Str(required=True, validate=validate.Length(PasswordResetValidation.PASSWORD_RESET_TOKEN_MIN_LENGTH, PasswordResetValidation.PASSWORD_RESET_TOKEN_MAX_LENGTH, error=PasswordResetValidation.PASSWORD_RESET_TOKEN_VALIDATION_MSG))
    new_password = fields.Str(required=True, validate=validate.Length(UserValidation.PASSWORD_MIN_LENGTH, max=UserValidation.PASSWORD_MAX_LENGTH, error=UserValidation.PASSWORD_VALIDATION_MSG))

    @post_load
    def make_update_unauthenticated_user_password_request(self, data, **kwargs):
        return UpdateUnauthenticatedUserPasswordRequest(**data)

