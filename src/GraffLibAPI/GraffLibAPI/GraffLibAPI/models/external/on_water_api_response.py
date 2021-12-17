import datetime as dt

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from GraffLibAPI.models.enums.marker_status import MarkerStatus
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.marker.marker_metadata_model  import MarkerMetadataModelSchema
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModelSchema
from marshmallow import post_load

class OnWaterApiResponse():
    def __init__(self, query, request_id, lat, lon, water):
       self.query = query
       self.request_id = request_id
       self.lat = lat
       self.lon = lon
       self.water = water

    def __repr__(self):
        return '<OnWaterApiResponse(name={self.query!r})>'.format(self=self)

class OnWaterApiResponseSchema(Schema):
    query = fields.Str(required=True)
    request_id = fields.Str(required=True)
    lat = fields.Decimal(required=True)
    lon = fields.Decimal(required=True)
    water = fields.Boolean(required=True)

    @post_load
    def make_create_on_water_api_response(self, data, **kwargs):
        return OnWaterApiResponse(**data)