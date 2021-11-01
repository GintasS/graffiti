# Library includes.
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow_enum import EnumField

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.marker_status import MarkerStatus

# TODO: [REFACTORING] Add timestamp to marker status. How can we track changes to marker status/graffiti status?

class UpdateMarkerStatusRequest():
    def __init__(self, marker_status):
        self.marker_status = marker_status

    def __repr__(self):
        return '<UpdateMarkerStatusRequest(name={self.marker_status!r})>'.format(self=self)


# **kwargs absorbs unmatched fields.
class UpdateMarkerStatusRequestSchema(Schema):
    marker_status = EnumField(MarkerStatus, required=True)

    @post_load
    def make_update_marker_status_request(self, data, **kwargs):
        return UpdateMarkerStatusRequest(**data)
