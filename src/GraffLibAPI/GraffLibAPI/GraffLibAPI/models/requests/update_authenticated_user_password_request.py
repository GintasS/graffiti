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
    user_id = fields.Int(required=True)
    old_password = fields.Str(required=True, validate=validate.Length(UserValidation.PASSWORD_MIN_LENGTH, UserValidation.PASSWORD_MAX_LENGTH, error=UserValidation.PASSWORD_VALIDATION_MSG))
    new_password = fields.Str(required=True, validate=validate.Length(UserValidation.PASSWORD_MIN_LENGTH, UserValidation.PASSWORD_MAX_LENGTH, error=UserValidation.PASSWORD_VALIDATION_MSG))
    changed_at = fields.DateTime(format=MiscValidation.DATE_FORMAT)

    @post_load
    def make_create_user_request(self, data, **kwargs):
        return UpdateAuthenticatedUserPasswordRequest(**data)

