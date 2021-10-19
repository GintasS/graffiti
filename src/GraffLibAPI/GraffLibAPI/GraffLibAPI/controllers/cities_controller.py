# Library imports
import json
from flask import Blueprint, render_template, request, jsonify
from linq import Flow
import datetime as dt
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError
from secrets import token_urlsafe
import bcrypt
import hashlib

# Project imports
from GraffLibAPI.models.enums import *
from GraffLibAPI.models.requests.create_city_request import *
from GraffLibAPI.models.responses.create_city_response import *
from GraffLibAPI.models.city_model import CityModel
from GraffLibAPI.database.entities.city_entity import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.mappings.mappings import *

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_cities = Blueprint('api-cities', __name__, url_prefix='/v1/cities')

@blueprint_cities.route('', methods=['POST'])
def create_city():
    try:
        city_request = CreateCityRequestSchema().load(request.get_json())
        found_city = session.query(CityEntity).\
            filter(
                or_(
                    CityEntity.city_name.like(city_request.city_name),
                )
            ).\
            first()

        if found_city is not None:
            return "City already exists", 409

        new_city = to_city_entity(city_request)
        session.add(new_city)
        session.commit()

        return to_create_city_response(new_city).toJSON(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500


@blueprint_cities.route('', methods=['GET'])
def get_city():
    try:
        cities = session.query(CityEntity).all()
        city_entity_schema = CityEntitySchema(many=True)
    except:
        return "Internal server errror.", 500
    return {
        'message': 'This PATCH13 endpoint should update the entity',
        'method': request.method,
        'body': city_entity_schema.dump(cities)
    }
