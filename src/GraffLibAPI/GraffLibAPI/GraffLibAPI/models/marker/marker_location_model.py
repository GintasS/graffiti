import datetime as dt
import sqlalchemy as sa

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError, post_load
from marshmallow.fields import Nested
from GraffLibAPI.models.enums.role_type import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from marshmallow import Schema
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema


class MarkerLocationModel():
    def __init__(self, country, city, address, coordinates):
        self.country = country
        self.city = city
        self.address = address
        self.coordinates = coordinates

    def __repr__(self):
        return '<MarkerLocationModel(name={self.coordinates!r})>'.format(self=self)

class MarkerLocationModelSchema(Schema):
    country = fields.Str(required=True, validation=validate.Length(LocationValidation.COUNTRY_NAME_MIN_LENGTH, LocationValidation.COUNTRY_NAME_MAX_LENGTH, error=LocationValidation.COUNTRY_NAME_VALIDATION_MSG))
    city = fields.Str(required=True, validation=validate.Length(LocationValidation.CITY_NAME_MIN_LENGTH, LocationValidation.CITY_NAME_MAX_LENGTH, error=LocationValidation.CITY_NAME_VALIDATION_MSG))
    address = fields.Str(required=True, validation=validate.Length(LocationValidation.STREET_ADDRESS_MIN_LENGTH, LocationValidation.STREET_ADDRESS_MAX_LENGTH, error=LocationValidation.STREET_ADDRESS_VALIDATION_MSG))
    coordinates = fields.List(required=True, cls_or_instance=fields.Decimal(as_string=True), validate=validate.Length(LocationValidation.COORDINATES_LIST_MIN_ELEMENTS, LocationValidation.COORDINATES_LIST_MAX_ELEMENTS, error=LocationValidation.COORDINATES_VALIDATION_MSG))

    @post_load
    def make_marker_location_model(self, data, **kwargs):
        return MarkerLocationModel(**data)