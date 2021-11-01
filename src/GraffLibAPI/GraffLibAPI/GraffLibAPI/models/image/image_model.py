import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.role_type import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.image.image_metadata_model import ImageMetadataModelSchema
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModelSchema
from marshmallow_enum import EnumField
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus


class ImageModel():
    def __init__(self, photo_url, marker_id, graffiti_status, image_metadata_model, image_classification_model):
       self.photo_url = photo_url
       self.marker_id = marker_id
       self.graffiti_status = graffiti_status
       self.image_metadata_model = image_metadata_model
       self.image_classification_model = image_classification_model

    def __repr__(self):
        return '<ImageModel(name={self.photo_url!r})>'.format(self=self)

class ImageModelSchema(Schema):
    photo_url = fields.Url(required=True)
    marker_id = fields.Str(required=True, validation=validate.Length(MarkerValidation.MARKER_ID_MIN_LENGTH, MarkerValidation.MARKER_ID_MAX_LENGTH, error=MarkerValidation.MARKER_ID_VALIDATION_MSG))
    graffiti_status = EnumField(GraffitiStatus, required=True)
    image_metadata_model = fields.Nested(nested=ImageMetadataModelSchema(), required=True)
    image_classification_model = fields.Nested(nested=ImageClassificationModelSchema(), required=True)