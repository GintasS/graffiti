import json

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema

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
    user_id = fields.Int()
    user_name = fields.Str()
    email = fields.Email()
    created_at = fields.Date()