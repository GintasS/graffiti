import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums import RoleType
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModelSchema 
from marshmallow_enum import EnumField
from GraffLibAPI.models.enums.image_direction import ImageDirection
from GraffLibAPI.models.enums import image_direction

class ImageClassificationModel():
    def __init__(self, user_provided_name, description, graffiti_object, image_direction):
        self.user_provided_name = user_provided_name
        self.description = description
        self.graffiti_object = graffiti_object
        self.image_direction = image_direction

    def __repr__(self):
        return '<ImageClassificationModel(name={self.extension!r})>'.format(self=self)

class ImageClassificationModelSchema(Schema):
    user_provided_name = fields.Str()
    description = fields.Str()
    graffiti_object = fields.Str()
    image_direction = EnumField(image_direction.ImageDirection)