# Library includes.
import datetime as dt
from geoalchemy2.shape import to_shape

# Project includes.
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest
from GraffLibAPI.models.requests.create_city_request import CreateCityRequest
from GraffLibAPI.models.responses.create_user_response import CreateUserResponse
from GraffLibAPI.models.responses.create_city_response import CreateCityResponse
from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.database.entities.city_entity import CityEntity
from GraffLibAPI.database.entities.user_password_reset_history_entity import UserPasswordResetHistoryEntity
from GraffLibAPI.database.entities.user_password_reset_entity import UserPasswordResetEntity
from GraffLibAPI.database.entities.image.image_entity import ImageEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModel
from GraffLibAPI.models.image_models.image_model import ImageModel
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModel
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModel
from GraffLibAPI.models.requests.images.create_user_image_request import CreateUserImageRequest
from GraffLibAPI.models.enums.user_password_reset_type import UserPasswordResetType
from GraffLibAPI.models.responses.images.create_user_image_response import CreateUserImageResponse
from GraffLibAPI.database.db_setup import session

# http://www.python.org/dev/peps/pep-3107/
def to_user_entity(request : CreateUserRequest) -> UserEntity:
    return UserEntity(
        user_name=request.user_name, 
        first_name=request.first_name, 
        last_name=request.last_name, 
        email=request.email, 
        password=request.password, 
        role=request.role,
        created_at=dt.datetime.now())

def to_city_entity(request : CreateCityRequest) -> CityEntity:
    return CityEntity(
        city_name=request.city_name)

def to_create_user_response(entity : UserEntity) -> CreateUserResponse:
    return CreateUserResponse(
        entity.id, 
        entity.user_name, 
        entity.email,
        entity.created_at)

def to_create_city_response(entity : CityEntity) -> CreateCityResponse:
    return CreateCityResponse(
        entity.id,
        entity.city_name)

# User Password Resets

def create_user_password_reset_entity(user_id : int, reset_type : str, token : str) -> UserPasswordResetEntity:
    return UserPasswordResetEntity(
        user_id = user_id,
        reset_type = reset_type,
        token = token)

def create_user_password_reset_history_entity(reset_type : UserPasswordResetType, reset_id : int) -> UserPasswordResetHistoryEntity:
    current_date = dt.datetime.now()
    
    return UserPasswordResetHistoryEntity(
        reset_iniatiated = current_date,
        reset_completed =  None if reset_type == UserPasswordResetType.UNAUTHENTICATED else current_date,
        reset_id = reset_id)

# Images

def to_image_model(image_entity : ImageEntity) -> ImageModel:
    image_metadata_entity = session.query(ImageMetadataEntity).\
            filter(
                ImageMetadataEntity.image_unique_name == image_entity.image_unique_name
            ).\
            first()

    image_location_entity = session.query(ImageLocationEntity).\
        filter(
            ImageLocationEntity.id == image_metadata_entity.id
        ).\
        first()

    image_classification_entity = session.query(ImageClassificationEntity).\
        filter(
            ImageClassificationEntity.image_unique_name == image_entity.image_unique_name
        ).\
        first()

    # TODO: what happens here if some entities are missing?

    coordinates = to_shape(image_location_entity.coordinates)
    coordinates_list = [ coordinates.x, coordinates.y ]

    image_location_model = to_image_location_model(coordinates_list)
    image_metadata_model = to_image_metadata_model(image_metadata_entity, image_location_model)
    image_classification_model = to_image_classification_model(image_classification_entity)

    return ImageModel("", image_entity, image_metadata_model, image_classification_model)

def to_image_metadata_model(image_metadata_entity : ImageMetadataEntity, image_location_model) -> ImageMetadataModel:   
    return ImageMetadataModel(image_metadata_entity.extension, image_metadata_entity.original_image_name, image_metadata_entity.photographed_time, image_metadata_entity.upload_time, image_location_model)

def to_image_classification_model(image_classification_entity : ImageClassificationEntity) -> ImageClassificationModel:
    return ImageClassificationModel(image_classification_entity.user_provided_name, image_classification_entity.description, image_classification_entity.graffiti_object, image_classification_entity.direction)

def to_image_location_model(coordinates) -> ImageLocationModel:
    return ImageLocationModel(coordinates)

def to_image_entity(create_user_image_request : CreateUserImageRequest, image_unique_name : str, url: str) -> ImageEntity:
    return ImageEntity(
        image_unique_name = image_unique_name,
        user_id = create_user_image_request.user_id,
        url = url)

def to_image_metadata_entity(image_metadata_model : ImageMetadataModel, image_unique_name : str) -> ImageMetadataEntity:
    return ImageMetadataEntity(
        image_unique_name = image_unique_name,
        original_image_name = image_metadata_model.original_image_name,
        extension = image_metadata_model.extension,
        photographed_time = image_metadata_model.photographed_time,
        upload_time = image_metadata_model.upload_time)

def to_image_location_entity(coordinates, image_metadata_id : int) -> ImageLocationEntity:
    return ImageLocationEntity(
        id = image_metadata_id,
        coordinates = 'SRID=4326;POINT({} {})'.format(coordinates[0], coordinates[1]))

def to_image_classification_entity(image_classification_model : ImageClassificationModel, image_unique_name : str) -> ImageClassificationModel:
    return ImageClassificationEntity(
        image_unique_name = image_unique_name,
        user_provided_name = image_classification_model.user_provided_name,
        description = image_classification_model.description,
        graffiti_object = image_classification_model.graffiti_object,
        direction = image_classification_model.image_direction)

def create_user_image_response(image_unique_name : str, url : str, image_metadata_model : ImageMetadataModel, image_classification_model : ImageClassificationModel ) -> CreateUserImageResponse:
        return CreateUserImageResponse(image_unique_name, url, image_metadata_model, image_classification_model)