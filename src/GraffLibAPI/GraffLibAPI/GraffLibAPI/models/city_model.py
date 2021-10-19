# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow_enum import EnumField
from GraffLibAPI.configuration.constants import *

class CityModel():
    def __init__(self, city_name):

        self.city_name = city_name

    def __repr__(self):
        return '<City(name={self.city_name!r})>'.format(self=self)

class CityModelSchema(Schema):

    city_name = fields.Str()
