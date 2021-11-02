# Library includes.
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError

# Project includes.
from GraffLibAPI.configuration.constants import *

class CreateMarkerRequest():
    def __init__(self, user_id, coordinates):
        self.user_id = user_id,
        self.coordinates = coordinates

    def __repr__(self):
        return '<CreateMarkerRequest(name={self.coordinates!r})>'.format(self=self)


# **kwargs absorbs unmatched fields.
class CreateMarkerRequestSchema(Schema):
    user_id = fields.Int(required=True)
    coordinates = fields.List(required=True, cls_or_instance=fields.Decimal(as_string=True), validate=validate.Length(LocationValidation.COORDINATES_LIST_MIN_ELEMENTS, LocationValidation.COORDINATES_LIST_MAX_ELEMENTS, error=LocationValidation.COORDINATES_VALIDATION_MSG))

    @post_load
    def make_create_marker_request(self, data, **kwargs):
        return CreateMarkerRequest(**data)
