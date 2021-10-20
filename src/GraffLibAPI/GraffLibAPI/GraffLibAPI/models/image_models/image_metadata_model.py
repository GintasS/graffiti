import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModel, ImageLocationModelSchema
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema

class ImageMetadataModel():
    def __init__(self, extension, photographed_time, upload_time, image_location_model):
        self.extension = extension
        self.photographed_time = photographed_time
        self.upload_time = upload_time
        self.image_location_model = image_location_model

    def __repr__(self):
        return '<ImageMetadataModel(name={self.extension!r})>'.format(self=self)

class ImageMetadataModelSchema(Schema):
    extension = fields.Str(validate=validate.Length(min=IMAGE_EXTENSION_MIN_LENGTH, max=IMAGE_EXTENSION_MAX_LENGTH, error=IMAGE_EXTENSION_VALIDATION_MSG))
    photographed_time = fields.Date()
    upload_time = fields.Date()
    image_location_model = fields.Nested(ImageLocationModelSchema)