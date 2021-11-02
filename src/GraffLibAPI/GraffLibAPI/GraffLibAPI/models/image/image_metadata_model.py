import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.role_type import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image.image_location_model import ImageLocationModel, ImageLocationModelSchema
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema

class ImageMetadataModel():
    def __init__(self, extension, original_image_name, photographed_time, upload_time, image_location_model):
        self.extension = extension
        self.original_image_name = original_image_name
        self.photographed_time = photographed_time
        self.upload_time = upload_time
        self.image_location_model = image_location_model

    def __repr__(self):
        return '<ImageMetadataModel(name={self.extension!r})>'.format(self=self)

class ImageMetadataModelSchema(Schema):
    extension = fields.Str(required=True, validate=validate.Length(ImageValidation.IMAGE_EXTENSION_MIN_LENGTH, ImageValidation.IMAGE_EXTENSION_MAX_LENGTH, error=ImageValidation.IMAGE_EXTENSION_VALIDATION_MSG))
    original_image_name = fields.String(required=True, validate=validate.Length(ImageValidation.IMAGE_ORIGINAL_NAME_MIN_LENGTH, ImageValidation.IMAGE_ORIGINAL_NAME_MAX_LENGTH, error=ImageValidation.IMAGE_ORIGINAL_NAME_VALIDATION_MSG))
    photographed_time = fields.DateTime(required=True, format=MiscValidation.DATE_FORMAT)
    upload_time = fields.DateTime(required=True, format=MiscValidation.DATE_FORMAT)
    image_location_model = fields.Nested(nested=ImageLocationModelSchema, required=True)