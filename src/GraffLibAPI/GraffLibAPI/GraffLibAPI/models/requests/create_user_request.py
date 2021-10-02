import datetime as dt
import json

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema

class CreateUserRequest(UserModel):
    def __init__(self, user_name, first_name, last_name, email, password, role):
        super(CreateUserRequest, self).__init__(user_name, first_name, last_name, email, password, role)

    def __repr__(self):
        return '<CreateUserRequest(name={self.user_name!r})>'.format(self=self)



# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.
class CreateUserRequestSchema(UserModelSchema):
    @post_load
    def make_create_user_request(self, data, **kwargs):
        return CreateUserRequest(**data)
