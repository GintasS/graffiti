# Library imports
from flask import Blueprint, request
from linq import Flow
from secrets import token_urlsafe
import json
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
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModel
from GraffLibAPI.database.entities.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.models.requests.images.create_user_image_request import CreateUserImageRequest, CreateUserImageRequestSchema
from GraffLibAPI.models.responses.images.create_user_image_response import CreateUserImageResponse, CreateUserImageResponseSchema
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.utils.image_helper import *

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
        user_image_request = CreateUserImageRequestSchema().load(request.get_json())
        user_image_request.user_id = user_id

        # Validation:
            # TODO: Check if file has a virus.
            # TODO: Validate file (size, extension and so on).
            # TODO: Validate Metadata
            # TODO: Validate Classification
        # Status codes:
            # TODO: Check whether the user has a particular image.
            # TODO: Throw status codes.
        # Creation:
            # TODO: Generate a name for the image (so that users can't iterate through them).
            # TODO: Generate url to access the image.        
        # City/Marker:
            # TODO: Get city name from the coordinates.
            # TODO: Assign image to the marker (or create a new marker if it's the first image).
        # File
            # TODO: Clean any sensitive data in the file's metadata.
            # TODO: Save image to a specific folder.
        # Misc
            # TODO: Should we send coordinates through JSON or take them from File's metadata?

        # Creating unique image name.
        # TODO: Should we make unique image name smaller?
        unique_image_name = token_urlsafe(32)

        # Create url.
        url = create_image_unique_url(unique_image_name, user_image_request.image_metadata_model.extension)

        # Creating new image entity.
        new_image = to_image_entity(user_image_request, unique_image_name)
        session.add(new_image)
        session.commit()

        # Create relashionships.
        image_metadata_entity = to_image_metadata_entity(user_image_request.image_metadata_model, unique_image_name)
        session.add(image_metadata_entity)
        session.commit()

        image_location_entity = to_image_location_entity(user_image_request.image_metadata_model.image_location_model.coordinates, image_metadata_entity.id)
        session.add(image_location_entity)
        session.commit()

        image_classification_entity = to_image_classification_entity(user_image_request.image_classification_model, unique_image_name)
        session.add(image_classification_entity)
        session.commit()

        response = create_user_image_response(unique_image_name, url, user_image_request.image_metadata_model, user_image_request.image_classification_model)
        return CreateUserImageResponseSchema().dump(response), 201
    except:
        return "Internal server errror.", 500
