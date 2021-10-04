import datetime as dt
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.configuration.constants import *

class UpdateAuthenticatedUserPasswordRequest():
    def __init__(self, user_id, old_password, new_password):
       self.user_id = user_id
       self.old_password = old_password;
       self.new_password = new_password;
       self.changed_at = dt.datetime.now()

    def __repr__(self):
        return '<UpdateAuthenticatedUserPasswordRequest(name={self.user_id!r})>'.format(self=self)

class UpdateAuthenticatedUserPasswordRequestSchema(Schema):
    user_id = fields.Int()
    old_password = fields.Str(validate=validate.Length(min=PASSWORD_MIN_LENGTH, max=PASSWORD_MAX_LENGTH, error=PASSWORD_VALIDATION_MSG))
    new_password = fields.Str(validate=validate.Length(min=PASSWORD_MIN_LENGTH, max=PASSWORD_MAX_LENGTH, error=PASSWORD_VALIDATION_MSG))
    changed_at = fields.Date()

    @post_load
    def make_create_user_request(self, data, **kwargs):
        return UpdateAuthenticatedUserPasswordRequest(**data)

