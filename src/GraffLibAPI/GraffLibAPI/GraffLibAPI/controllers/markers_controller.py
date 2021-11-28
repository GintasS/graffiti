from typing import Type
from flask import Blueprint, render_template, request, jsonify
from secrets import token_urlsafe
from marshmallow import ValidationError
import json


from GraffLibAPI.database.db_setup import session
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.database.entities.marker.marker_entity import MarkerEntity, MarkerEntitySchema
from GraffLibAPI.models.marker.marker_model import MarkerModel, MarkerModelSchema
from GraffLibAPI.database.entities.marker.marker_entity import MarkerEntity
from GraffLibAPI.database.entities.marker.marker_location_entity import MarkerLocationEntity
from GraffLibAPI.database.entities.marker.marker_metadata_entity import MarkerMetadataEntity
from GraffLibAPI.models.requests.create_marker_request import CreateMarkerRequest, CreateMarkerRequestSchema
from GraffLibAPI.models.marker.marker_location_model import MarkerLocationModel
from GraffLibAPI.models.marker.marker_model import MarkerModel
from GraffLibAPI.models.marker.marker_metadata_model import MarkerMetadataModel
from GraffLibAPI.utils.location_helper import *
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.database.entities.city_entity import CityEntity, CityEntitySchema
from GraffLibAPI.models.requests.update_marker_status_request import UpdateMarkerStatusRequest, UpdateMarkerStatusRequestSchema

blueprint_markers = Blueprint("api-markers", __name__, url_prefix="/v1/markers")

@blueprint_markers.route("", methods=["GET"])
def get_markers():
    try:
        markers_join = session.query(
                MarkerLocationEntity, MarkerMetadataEntity, MarkerEntity
            ).filter(
                MarkerMetadataEntity.marker_id == MarkerEntity.id
            ).filter(
                 MarkerLocationEntity.id == MarkerMetadataEntity.id
            ).all()

        marker_models = []

        for m in markers_join:
            marker_models.append(to_marker_model(m[2], m[1], m[0]))

        return { "body": MarkerModelSchema(many=True).dump(marker_models) }, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_markers.route("", methods=["POST"])
def create_marker():

    # TODO: [NEW ENDPOINTS] check if country exists
    # TODO: [OAuth] remove user_id from json body after integrating to open auth.

    try:
        create_marker_request = CreateMarkerRequestSchema().load(request.get_json())
        new_marker_coordinates = [ create_marker_request.coordinates[0], create_marker_request.coordinates[1] ]

        # Reverse engineer address from coordinates.
        location = get_location_from_coordinates(create_marker_request.coordinates[0], create_marker_request.coordinates[1])
        location_raw = location.raw["address"]
        location_address = get_short_address(location_raw)

        if location is None or location_address is None:
            return "Unable to get address from coordinates.", 409

        city = location_raw["city"].strip()
        country = location_raw["country"].strip()
        address = location_address.strip()

        found_city = session.query(CityEntity).\
            filter(
                CityEntity.city_name == city
            ).\
            first()
        # TODO: [OAuth] remove user_id from json multi-part HTTP request after integrating to open auth.
        found_user = session.query(UserEntity).\
            filter(
                UserEntity.id == create_marker_request.user_id
            ).\
            first()

        if found_city is None:
            return "City does not exist in database.", 404
        if found_user is None:
            return "User was not found.", 404


        markers_join = session.query(
                MarkerLocationEntity, MarkerMetadataEntity, MarkerEntity
            ).filter(
                MarkerLocationEntity.city == found_city.city_name
            ).filter(
                MarkerMetadataEntity.id == MarkerLocationEntity.id
            ).filter(
                MarkerEntity.id == MarkerMetadataEntity.marker_id
            ).all()
        
        # Get all markers from a city to which this marker is going to be added.
        # Calculate distances to all markers, to find the 
        if is_new_marker_too_close_to_existing_one(markers_join, new_marker_coordinates) is True:
            return "Marker already exists too close to this new marker ({} km), can't create a new one.".format(LocationValidation.NEW_MARKER_MIN_DISTANCE_BETWEEN_EXISTING_MARKER), 409

        # Generate marker id.
        marker_id = token_urlsafe(32)
        
        marker_entity = to_marker_entity(marker_id, create_marker_request.user_id)
        session.add(marker_entity)
        session.commit()

        marker_metadata_entity = to_marker_metadata_entity(marker_entity.id)
        session.add(marker_metadata_entity)
        session.commit()

        marker_location_entity = to_marker_location_entity(marker_metadata_entity.id, country, city, address, create_marker_request.coordinates)
        session.add(marker_location_entity)
        session.commit()

        marker_model = to_marker_model(marker_entity, marker_metadata_entity, marker_location_entity)

        return { "body": MarkerModelSchema().dump(marker_model) }, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_markers.route("/<string:marker_id>/status/marker-status", methods=["PATCH"])
def patch_marker_status(marker_id):
    try:
        update_marker_status_request = UpdateMarkerStatusRequestSchema().load(request.get_json())

        found_marker = session.query(MarkerEntity).\
            filter(
                MarkerEntity.id == marker_id
            ).\
            first()

        if found_marker is None:
            return "Marker was not found.", 404

        found_marker.marker_status = update_marker_status_request.marker_status
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_markers.route("/<string:marker_id>/", methods=["DELETE"])
def delete_marker(marker_id):
    try:

        # TODO: need to delete folder as well.

        found_marker = session.query(MarkerEntity).\
            filter(
                MarkerEntity.id == marker_id
            ).\
            first()

        if found_marker is None:
            return "Marker was not found.", 404

        marker_join = session.query(
                    MarkerEntity, MarkerMetadataEntity, MarkerLocationEntity
            ).filter(
                    MarkerEntity.id == marker_id
            ).filter(
                    MarkerMetadataEntity.marker_id == marker_id
            ).filter(
                    MarkerLocationEntity.id == MarkerMetadataEntity.id
            ).first()

        image_join = session.query(
                    ImageEntity, ImageMetadataEntity, ImageLocationEntity, ImageClassificationEntity
            ).filter(
                    ImageEntity.marker_id == marker_id
            ).filter(
                    ImageMetadataEntity.image_unique_name == ImageEntity.image_unique_name
            ).filter(
                    ImageLocationEntity.id ==  ImageMetadataEntity.id
            ).filter(
                    ImageClassificationEntity.image_unique_name == ImageEntity.image_unique_name
            ).all()

        if marker_join is None:
            return "Internal server errror.", 500

        for img in image_join:
            session.delete(img[3])
            session.delete(img[2])
            session.delete(img[1])
            session.delete(img[0])
            session.commit()

        session.delete(marker_join[2])
        session.delete(marker_join[1])
        session.delete(marker_join[0])
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500