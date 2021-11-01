# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema
from GraffLibAPI.models.image.image_metadata_model import ImageMetadataModelSchema
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModelSchema
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus
from marshmallow_enum import EnumField

class CreateMarkerResponse():
    def __init__(self, marker_id):
       self.marker_id = marker_id

class CreateMarkerResponseSchema(Schema):
    marker_id = fields.Str(required=True, validation=validate.Length(MarkerValidation.MARKER_ID_MIN_LENGTH, MarkerValidation.MARKER_ID_MAX_LENGTH, error=MarkerValidation.MARKER_ID_VALIDATION_MSG))
