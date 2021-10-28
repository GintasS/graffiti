import datetime as dt
import sqlalchemy as sa

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError, post_load
from marshmallow.fields import Nested
from GraffLibAPI.models.enums import RoleType
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *
from marshmallow import Schema
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema

class ImageLocationModel():
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __repr__(self):
        return '<ImageLocationModel(name={self.coordinates!r})>'.format(self=self)

    # TODO: Fix types in all schemas, marshmallow and SQL Alchemy has specific fields.

class ImageLocationModelSchema(Schema):
    coordinates = fields.List(fields.Decimal(as_string=True))

    @post_load
    def make_image_location_model(self, data, **kwargs):
        return ImageLocationModel(**data)