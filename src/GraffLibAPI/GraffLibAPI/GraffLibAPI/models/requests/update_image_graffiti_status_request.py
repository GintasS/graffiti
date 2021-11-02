# Library includes.
from marshmallow_enum import EnumField
from marshmallow import Schema, fields, validate, ValidationError, post_load

# Project includes.
from GraffLibAPI.models.user_model import UserModel, UserModelSchema
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus

class UpdateImageGraffitiStatusRequest():
    def __init__(self, graffiti_status):
        self.graffiti_status = graffiti_status

    def __repr__(self):
        return '<UpdateMarkerImageGraffitiStatusRequest(name={self.graffiti_status!r})>'.format(self=self)


# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.
class UpdateImageGraffitiStatusRequestSchema(Schema):
    graffiti_status = EnumField(GraffitiStatus, required=True)

    @post_load
    def make_update_image_graffiti_status(self, data, **kwargs):
        return UpdateImageGraffitiStatusRequest(**data)

