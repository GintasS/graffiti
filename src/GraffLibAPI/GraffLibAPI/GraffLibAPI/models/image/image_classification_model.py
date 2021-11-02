import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError, post_load
from GraffLibAPI.models.enums.role_type import RoleType
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema 
from marshmallow_enum import EnumField
from GraffLibAPI.models.enums.image_direction import ImageDirection

class ImageClassificationModel():
    def __init__(self, user_provided_name, description, graffiti_object, image_direction):
        self.user_provided_name = user_provided_name
        self.description = description
        self.graffiti_object = graffiti_object
        self.image_direction = image_direction

    def __repr__(self):
        return '<ImageClassificationModel(name={self.user_provided_name!r})>'.format(self=self)

class ImageClassificationModelSchema(Schema):
    user_provided_name = fields.Str(required=False, validate=validate.Length(ImageValidation.USER_PROVIDED_IMAGE_NAME_MIN_LENGTH, ImageValidation.USER_PROVIDED_IMAGE_NAME_MAX_LENGTH, error=ImageValidation.USER_PROVIDED_IMAGE_NAME_VALIDATION_MSG))
    description = fields.Str(required=False, validate=validate.Length(ImageValidation.IMAGE_DESCRIPTION_MIN_LENGTH, ImageValidation.IMAGE_DESCRIPTION_MAX_LENGTH, error=ImageValidation.IMAGE_DESCRIPTION_VALIDATION_MSG))
    graffiti_object = fields.Str(required=False, validate=validate.Length(ImageValidation.IMAGE_GRAFFITI_OBJECT_MIN_LENGTH, ImageValidation.IMAGE_GRAFFITI_OBJECT_MAX_LENGTH, error=ImageValidation.IMAGE_GRAFFITI_OBJECT_VALIDATION_MSG))
    image_direction = EnumField(ImageDirection, required=False)

    @post_load
    def make_image_classification_model(self, data, **kwargs):
        return ImageClassificationModel(**data)