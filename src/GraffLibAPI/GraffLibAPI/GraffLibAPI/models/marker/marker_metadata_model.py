import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.marker_status import MarkerStatus
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.marker.marker_location_model import MarkerLocationModelSchema

class MarkerMetadataModel():
    def __init__(self, marker_id, created_at, last_update, marker_location_model):
       self.marker_id = marker_id
       self.created_at = created_at
       self.last_update = last_update
       self.marker_location_model = marker_location_model

    def __repr__(self):
        return '<MarkerMetadataModel(name={self.created_at!r})>'.format(self=self)

class MarkerMetadataModelSchema(Schema):
    marker_id = fields.Str(required=True, validation=validate.Length(MarkerValidation.MARKER_ID_MIN_LENGTH, MarkerValidation.MARKER_ID_MAX_LENGTH, error=MarkerValidation.MARKER_ID_VALIDATION_MSG))
    created_at = fields.DateTime(required=True, format=MiscValidation.DATE_FORMAT)
    last_update = fields.DateTime(required=True, format=MiscValidation.DATE_FORMAT)
    marker_location_model = fields.Nested(nested=MarkerLocationModelSchema, required=True)