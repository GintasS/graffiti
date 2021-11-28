# Library imports.
from flask import Blueprint, render_template, request, jsonify
from secrets import token_urlsafe
import json
import datetime
from PIL import Image
from exif import Image as Img
import os
import os.path as pathh
from pathlib import Path
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError

# TODO: [CLEANING] Remove unused python libraries
# TODO: [MAJOR REFACTORING] Move logic code to services.
# TODO: [MAJOR REFACTORING] Add tests for services.
# TODO: Add image id for image model/responses.
# TODO: Model Validation does not work everywhere.

# Project imports.
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.database.entities.image.image_entity import ImageEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.models.image.image_location_model import ImageLocationModel, ImageLocationModelSchema
from GraffLibAPI.models.image.image_model import ImageModel, ImageModelSchema
from GraffLibAPI.models.image.image_metadata_model import ImageMetadataModel
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModel, ImageClassificationModelSchema
from GraffLibAPI.database.entities.user.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.models.responses.create_marker_image_response import CreateMarkerImageResponse, CreateMarkerImageResponseSchema
from GraffLibAPI.mappings.mappings import *
from requests_toolbelt.multipart import decoder
from GraffLibAPI.utils.file_helper import *
from GraffLibAPI.utils.image_helper import *
from GraffLibAPI.utils.datetime_parser import *
from GraffLibAPI.utils.location_helper import *
from GraffLibAPI.database.entities.marker.marker_entity import MarkerEntity
from GraffLibAPI.database.entities.marker.marker_metadata_entity import MarkerMetadataEntity
from GraffLibAPI.database.entities.marker.marker_location_entity import MarkerLocationEntity
from GraffLibAPI.models.marker.marker_model import MarkerModel, MarkerModelSchema
from GraffLibAPI.models.requests.update_image_graffiti_status_request import UpdateImageGraffitiStatusRequestSchema 

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_marker_images = Blueprint("api-marker-images", __name__, url_prefix="/v1")

@blueprint_marker_images.route("/markers/<string:marker_id>/images", methods=["GET"])
def get_marker_images(marker_id):
    try:
        found_marker = session.query(MarkerEntity).\
            filter(
                MarkerEntity.id == marker_id
            ).\
            first()

        if found_marker is None:
            return "Marker does not exist", 404

        marker_images = session.query(ImageEntity).\
            filter(
                ImageEntity.marker_id == marker_id
            ).\
            all()

        image_models = list(map(lambda image_entity: to_image_model(image_entity), marker_images))

        return { "body": ImageModelSchema(many=True).dump(image_models) }, 200  
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_marker_images.route("/markers/<string:marker_id>/images", methods=["POST"])
def create_marker_image(marker_id):
    try:
        # Validation:
            # TODO: [SECURITY] Check if file has a virus.								
        # Status codes:
            # TODO: [FILE] [Partially done, checking the name] Check whether the user has a particular image.
        # File
            # TODO: [SECURITY] Clean any sensitive data in the file"s metadata.
            # TODO: [FILE] File compression.
        # Misc
	        # TODO: [FILE] Should we make unique image name smaller?

        found_marker = session.query(MarkerEntity).\
            filter(
                MarkerEntity.id == marker_id
            ).\
            first()

        result = decoder.MultipartDecoder(request.get_data(), request.content_type)

        if len(result.parts) < 3 or len(result.parts) > 4:
            return "Bad Request", 400
        if found_marker is None:
            return "Marker was not found.", 404

        # Request data.
        # TODO: [OAuth] Change this to use authentication.
        user_id = int(result.parts[0].text)

        user_classification_model = ImageClassificationModelSchema().load(json.loads(result.parts[1].text))
        user_precise_location = None

        found_user = session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if found_user is None:
            return "User does not exist", 404

        if len(result.parts) == 4:
            user_precise_location = ImageLocationModelSchema().load(json.loads(result.parts[2].text))

        file_part = request.files["inFile"]
        request_headers = file_part.headers
        request_mime_type = request_headers[1][1]

        # File data.
        file_bytes = file_part.read()
        file_size = len(file_bytes) / 10000000
        file_name = file_part.filename.split(".")[0]

        # Finding image with the same name.
        image_join = session.query(
                 ImageEntity, ImageMetadataEntity
            ).filter(
                 ImageEntity.marker_id == marker_id
            ).filter(
                 ImageMetadataEntity.image_unique_name == ImageEntity.image_unique_name,
            ).filter(
                 ImageMetadataEntity.original_image_name == file_name,
            ).all()

        # Request validation.
        if len(image_join) >= 1:
            return "File already exists.", 409
        if is_http_request_mime_type(request_mime_type) == False:
            return "File type is wrong.", 415

        # File logic.
            # File EXIF data is here.
        file_metadata = Img(file_bytes)

        # Validating image with Pillow.
        file_opened_with_pillow = Image.open(file_part)
        file_extension = file_opened_with_pillow.format_description.split(" ")[0].lower()

        # TODO: check if all jsons passed to here are valid.


        if is_image_has_correct_extension(file_extension) == False:
            return "File type is wrong.", 415
        if request_mime_type.split("/")[1] != file_extension:
            return "File types don't match.", 415
        if file_size > 100:
            return "File size is too large", 413
        if file_metadata.has_exif == False:
            return "File metadata is missing.", 405
        if hasattr(file_metadata, "gps_latitude") == False and hasattr(file_metadata, "gps_longitude") == False and user_precise_location == None:
            return "File location data is missing.", 405
        
        gps_coordinates = None

        if hasattr(file_metadata, "gps_latitude") != False and hasattr(file_metadata, "gps_longitude") != False:
            gps_coordinates = [ dms_to_dd(file_metadata.gps_latitude, file_metadata.gps_latitude_ref), dms_to_dd(file_metadata.gps_longitude, file_metadata.gps_longitude_ref) ]

        if gps_coordinates is None and user_precise_location is not None:
            gps_coordinates = user_precise_location.coordinates

        # Image was taken on this date.
        file_metadata_date = parse_date(file_metadata.datetime_original)

        # Creating unique image name.
        unique_image_name = token_urlsafe(32)

        # Create a directory if not exists.
        directory = get_current_directory(marker_id)
        create_directory_if_not_exists(directory)

        # Save the image.
        save_file(file_bytes, directory, unique_image_name, file_extension)

        # Create relashionships.
        image_location_model_object = ImageLocationModel(gps_coordinates)
        image_metadata_model_object = ImageMetadataModel(file_extension, file_name, file_metadata_date, datetime.datetime.now(), image_location_model_object)
        
        new_entities = create_image_entities(unique_image_name, marker_id, user_classification_model, image_metadata_model_object, image_location_model_object, user_id)

        # Create response.
        response = create_marker_image_response(unique_image_name, new_entities[0].graffiti_status, user_id, image_metadata_model_object, user_classification_model)
        
        return { "body": CreateMarkerImageResponseSchema().dump(response) }, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_marker_images.route("/images/<string:image_id>/status/graffiti-status", methods=["PATCH"])
def patch_marker_image_graffiti_status(image_id):
    try:
        # TODO: [OAuth] Check if image belongs to the user.

        update_image_graffiti_status = UpdateImageGraffitiStatusRequestSchema().load(request.get_json())

        image = session.query(ImageEntity).\
            filter(
                ImageEntity.image_unique_name == image_id
            ).\
            first()

        if image is None:
            return "Image was not found.", 404

        image.graffiti_status = update_image_graffiti_status.graffiti_status
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

@blueprint_marker_images.route("/images/<string:image_id>/", methods=["DELETE"])
def delete_specific_image_for_marker(image_id):
    try:
        # TODO: [OAuth] Check if image belongs to the user.

        image = session.query(ImageEntity).\
            filter(
                ImageEntity.image_unique_name == image_id
            ).\
            first()

        if image == None:
            return "Image was not found.", 404

        image_join = session.query(
                 ImageEntity, ImageMetadataEntity, ImageClassificationEntity
            ).filter(
                 ImageEntity.image_unique_name == image_id
            ).filter(
                 ImageMetadataEntity.image_unique_name == image_id
            ).filter(
                 ImageClassificationEntity.image_unique_name == image_id,
            ).first()

        if image_join is None:
            return "Internal server errror.", 500

        image_location = session.query(
                ImageLocationEntity
            ).filter(
                ImageLocationEntity.id == image_join[1].id,
            ).first()

        if len(image_join) != 3 or image_location is None:
            return "Internal server errror.", 500
    
        # Order here is important because of FKs.
        # TODO: [MARKER] Should we delete markers if no images exist on the marker?

        session.delete(image_join[2])
        session.delete(image_location)
        session.delete(image_join[1])
        session.delete(image_join[0])
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500