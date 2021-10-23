# Library imports
from flask import Blueprint, request
from linq import Flow
from secrets import token_urlsafe
import json
import datetime
from PIL import Image
from exif import Image as Img
import os
import os.path as pathh
from pathlib import Path


# TODO: Remove unused python libraries

# Project imports.
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.database.entities.image.image_entity import ImageEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModel
from GraffLibAPI.models.image_models.image_model import ImageModel, ImageModelSchema
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModel
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModel, ImageClassificationModelSchema
from GraffLibAPI.database.entities.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.models.requests.images.create_user_image_request import CreateUserImageRequest
from GraffLibAPI.models.responses.images.create_user_image_response import CreateUserImageResponse, CreateUserImageResponseSchema
from GraffLibAPI.mappings.mappings import *
from requests_toolbelt.multipart import decoder
from GraffLibAPI.utils.file_helper import *
from GraffLibAPI.utils.image_helper import *
from GraffLibAPI.utils.datetime_parser import *

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_images = Blueprint('api-images', __name__, url_prefix='/v1/users')

@blueprint_images.route('/<int:user_id>/images', methods=['GET'])
def get_user_images(user_id):
    try:
        found_user = session.query(UserEntity).\
            filter(
                UserEntity.id == user_id
            ).\
            first()

        if found_user is None:
            return "User does not exist", 404

        user_images = session.query(ImageEntity).\
            filter(
                ImageEntity.user_id == user_id
            ).\
            all()

        image_models = list(map(lambda image_entity: to_image_model(image_entity), user_images))
        schema = ImageModelSchema(many=True)
    except:
        return "Internal server errror.", 500

    return {
        'message': 'This PATCH13 endpoint should update the entity',
        'method': request.method,
        'body': schema.dump(image_models)
    }

@blueprint_images.route('/<int:user_id>/images', methods=['POST'])
def create_user_image(user_id):
    try:
        # Validation:
            # TODO: Check if file has a virus.								
        # Status codes:
            # TODO: Check whether the user has a particular image. [Partially done, checking the name]
        # Creation:        
            # TODO: Generate url to access the image.        
        # City/Marker:
            # TODO: Get city name from the coordinates.
            # TODO: Assign image to the marker (or create a new marker if it's the first image).
        # File
            # TODO: Clean any sensitive data in the file's metadata.
            # TODO: File compression.
        # Misc
	        # TODO: Should we make unique image name smaller?

        found_user = session.query(UserEntity).\
            filter(
                UserEntity.id == user_id
            ).\
            first()

        result = decoder.MultipartDecoder(request.get_data(), request.content_type)

        if len(result.parts) != 2:
            return "Bad Request", 400
        if found_user == None:
            return "User was not found.", 404

        # Request data.
        user_classification_model = ImageClassificationModelSchema().load(json.loads(result.parts[0].text))
        user_image_request = CreateUserImageRequest(user_classification_model, user_id)

        file_part = request.files['inFile']
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
                 ImageEntity.user_id == user_id
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

        if is_image_has_correct_extension(file_extension) == False:
            return "File type is wrong.", 415
        if request_mime_type.split('/')[1] != file_extension:
            return "File types don't match.", 415
        if file_size > 100:
            return "File size is too large", 413
        if file_metadata.has_exif == False or file_metadata.gps_latitude is None or file_metadata.gps_longitude is None:
            return "File metadata is missing.", 405

        # GPS data.
        gps_coordinates = [ file_metadata.gps_latitude[2], file_metadata.gps_longitude[2] ]

        # Image was taken on this date.
        file_metadata_date = parse_date(file_metadata.datetime_original)

        # Creating unique image name.
        # TODO: Should we make unique image name smaller?
        unique_image_name = token_urlsafe(32)

        # Create a directory if not exists.
        directory = get_current_directory(user_id)
        create_directory_if_not_exists(directory)

        # Save the image.
        save_file(file_bytes, directory, unique_image_name, file_extension)

        # Create url.
        url = create_image_unique_url(unique_image_name, user_id, file_extension)

        # Create relashionships.
        image_location_model_object = ImageLocationModel(gps_coordinates)
        image_metadata_model_object = ImageMetadataModel(file_extension, file_name, file_metadata_date, datetime.datetime.now(), image_location_model_object)
  
        create_image_entities(image_metadata_model_object, image_location_model_object, user_image_request, unique_image_name, url)

        # Create response.
        response = create_user_image_response(unique_image_name, url, image_metadata_model_object, user_image_request.image_classification_model)
        
        return CreateUserImageResponseSchema().dump(response), 201
    except:
        return "Internal server errror.", 500
