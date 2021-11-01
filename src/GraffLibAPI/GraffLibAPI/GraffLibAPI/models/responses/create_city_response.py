import json

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow import post_load
from GraffLibAPI.models.city_model import CityModel, CityModelSchema
from GraffLibAPI.configuration.constants import *

class CreateCityResponse():
    def __init__(self, city_id, city_name):
       self.city_id = city_id
       self.city_name = city_name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)

class CreateCityResponseSchema():
    city_id = fields.Int(required=True)
    city_name = fields.Str(required=True, validation=validate.Length(LocationValidation.CITY_NAME_MIN_LENGTH, LocationValidation.CITY_NAME_MAX_LENGTH, error=LocationValidation.CITY_NAME_VALIDATION_MSG))

    @post_load
    def make_create_city_request(self, data, **kwargs):
        return CreateCityResponse(**data)