import json

# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow import post_load
from  marshmallow.validate import Range
from GraffLibAPI.models.city_model import CityModel, CityModelSchema
from GraffLibAPI.configuration.constants import *

class CompareTwoImagesResponse():
    def __init__(self, similarity_index):
       self.similarity_index = similarity_index

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)

class CompareTwoImagesResponseSchema(Schema):
    similarity_index = fields.Int(required=True, strict=True, validate=[Range(min=0, error="Value must be greater than 0")])

    @post_load
    def make_compare_two_images_response(self, data, **kwargs):
        return CompareTwoImagesResponse(**data)
