import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.marker_status import MarkerStatus
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.marker.marker_metadata_model  import MarkerMetadataModelSchema
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModelSchema


class MarkerModel():
    def __init__(self, id, user_id, marker_status, marker_metadata_model):
       self.id = id
       self.user_id = user_id
       self.marker_status = marker_status
       self.marker_metadata_model = marker_metadata_model

    def __repr__(self):
        return '<MarkerModel(name={self.photo_url!r})>'.format(self=self)

class MarkerModelSchema(Schema):
    id = fields.Str(required=True, validation=validate.Length(MarkerValidation.MARKER_ID_MIN_LENGTH, MarkerValidation.MARKER_ID_MAX_LENGTH, error=MarkerValidation.MARKER_ID_VALIDATION_MSG))
    user_id = fields.Int(required=True)
    marker_status = EnumField(MarkerStatus, required=True)
    mark_metadata_model = fields.Nested(nested=MarkerMetadataModelSchema(), required=True)