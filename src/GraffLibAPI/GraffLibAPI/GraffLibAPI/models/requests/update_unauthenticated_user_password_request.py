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
    token = fields.Str()
    new_password = fields.Str(validate=validate.Length(min=PASSWORD_MIN_LENGTH, max=PASSWORD_MAX_LENGTH, error=PASSWORD_VALIDATION_MSG))

    @post_load
    def make_update_unauthenticated_user_password_request(self, data, **kwargs):
        return UpdateUnauthenticatedUserPasswordRequest(**data)

