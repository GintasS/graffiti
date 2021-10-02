import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums import RoleType

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
    user_name = fields.Str(validate=validate.Length(min=6, max=256, error="Username must be between 6 and 256 characters."))
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email(error="Email address must be a valid one.");
    password = fields.Str(validate=validate.Length(min=8, max=128, error="Password must be between 8 and 128 characters."))
    role = fields.Str(validate=validate.OneOf(["User", "Admin"], error="User role must be either:'User' or 'Admin'."))
    created_at = fields.Date()
