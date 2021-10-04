from GraffLibAPI.models.requests.create_user_request import CreateUserRequest
from GraffLibAPI.models.responses.create_user_response import CreateUserResponse
from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.database.entities.user_password_change_history_entity import UserPasswordChangeHistoryEntity

import datetime as dt

# http://www.python.org/dev/peps/pep-3107/
def from_create_user_request_to_user_entity(request : CreateUserRequest) -> UserEntity:
    return UserEntity(
        user_name=request.user_name, 
        first_name=request.first_name, 
        last_name=request.last_name, 
        email=request.email, 
        password=request.password, 
        role=request.role, 
        created_at=dt.datetime.now())

def from_user_entity_to_create_user_response(entity : UserEntity) -> CreateUserResponse:
    return CreateUserResponse(
        entity.id, 
        entity.user_name, 
        entity.email)

def from_user_entity_to_user_password_change_history_entity(entity : UserEntity) -> UserPasswordChangeHistoryEntity:
    return UserPasswordChangeHistoryEntity(
        user_id = entity.id, 
        password_changed_at = dt.datetime.now())

