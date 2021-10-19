# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, post_load
from GraffLibAPI.models.city_model import CityModel, CityModelSchema

class CreateCityRequest(CityModel):
    def __init__(self, city_name):
        super(CreateCityRequest, self).__init__(city_name)

    def __repr__(self):
        return '<CreateCityRequest(city_name={self.city_name!r})>'.format(self=self)

# **kwargs absorbs unmatched fields.
class CreateCityRequestSchema(CityModelSchema):
    @post_load
    def make_create_city_request(self, data, **kwargs):
        return CreateCityRequest(**data)
