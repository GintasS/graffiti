import datetime as dt
import simplejson

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModelSchema
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModelSchema

class ImageModel():
    def __init__(self, photo_url, user_id, image_metadata_model, image_classification_model):
       self.photo_url = photo_url
       self.image_metadata_model = image_metadata_model
       self.image_classification_model = image_classification_model

    def __repr__(self):
        return '<ImageModel(name={self.photo_url!r})>'.format(self=self)

class ImageModelSchema(Schema):
    photo_url = fields.Str()
    image_metadata_model = fields.Nested(ImageMetadataModelSchema())
    image_classification_model = fields.Nested(ImageClassificationModelSchema())