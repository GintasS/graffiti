# Library includes.
import datetime as dt

# Project includes.
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest
from GraffLibAPI.models.requests.create_city_request import CreateCityRequest
from GraffLibAPI.models.responses.create_user_response import CreateUserResponse
from GraffLibAPI.models.responses.create_city_response import CreateCityResponse
from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.database.entities.city_entity import CityEntity
from GraffLibAPI.database.entities.user_password_reset_history_entity import UserPasswordResetHistoryEntity
from GraffLibAPI.database.entities.user_password_reset_entity import UserPasswordResetEntity
from GraffLibAPI.models.enums.user_password_reset_type import UserPasswordResetType

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
        entity.email)

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
