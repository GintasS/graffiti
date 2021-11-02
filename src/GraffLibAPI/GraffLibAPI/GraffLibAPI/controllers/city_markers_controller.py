# Library imports.
import json
from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError

# Project imports.
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.database.entities.city_entity import CityEntity
from GraffLibAPI.database.entities.marker.marker_entity import MarkerEntity
from GraffLibAPI.database.entities.marker.marker_metadata_entity import MarkerMetadataEntity
from GraffLibAPI.database.entities.marker.marker_location_entity import MarkerLocationEntity
from GraffLibAPI.models.marker.marker_model import MarkerModel, MarkerModelSchema
from GraffLibAPI.mappings.mappings import *

blueprint_city_markers = Blueprint("api-city-markers", __name__, url_prefix="/v1/cities")

@blueprint_city_markers.route("/<int:id>/markers", methods=["GET"])
def get_markers_for_city(id):
    try:
        found_city = session.query(CityEntity).\
            filter(
                CityEntity.id == id
            ).\
            first()

        if found_city is None:
            return "City was not found.", 404

        markers_join = session.query(
                MarkerLocationEntity, MarkerMetadataEntity, MarkerEntity
            ).filter(
                MarkerLocationEntity.city == found_city.city_name
            ).filter(
                MarkerMetadataEntity.id == MarkerLocationEntity.id
            ).filter(
                MarkerEntity.id == MarkerMetadataEntity.marker_id
            ).all()


        marker_models = []

        for m in markers_join:
            marker_models.append(to_marker_model(m[2], m[1], m[0]))

        return { "body": MarkerModelSchema(many=True).dump(marker_models) }, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500