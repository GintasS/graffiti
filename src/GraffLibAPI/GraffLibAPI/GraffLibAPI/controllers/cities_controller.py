# Library imports.
import json
from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError

# Project imports.
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.database.entities.city_entity import CityEntity, CityEntitySchema
from GraffLibAPI.models.requests.create_city_request import CreateCityRequestSchema
from GraffLibAPI.mappings.mappings import *

blueprint_cities = Blueprint("api-cities", __name__, url_prefix="/v1/cities")

@blueprint_cities.route("", methods=["GET"])
def get_cities():
    try:
        cities = session.query(CityEntity).all()

        return { "body": CityEntitySchema(many=True).dump(cities) }, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500

@blueprint_cities.route("", methods=["POST"])
def create_city():
    try:
        city_request = CreateCityRequestSchema().load(request.get_json())
        found_city = session.query(CityEntity).\
            filter(
                CityEntity.city_name.like(city_request.city_name),
            ).\
            first()

        if found_city is not None:
            return "City already exists", 409

        city_entity = to_city_entity(city_request)

        session.add(city_entity)
        session.commit()

        return { "body": CityEntitySchema().dump(city_entity) }, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500

@blueprint_cities.route("/<int:city_id>/", methods=["DELETE"])
def delete_city(city_id):
    try:
        found_city = session.query(CityEntity).\
            filter(
                CityEntity.id == city_id
            ).\
            first()

        if found_city is None:
            return "City was not found.", 404

        session.delete(found_city)
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500