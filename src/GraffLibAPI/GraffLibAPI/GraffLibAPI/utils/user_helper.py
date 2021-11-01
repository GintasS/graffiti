from GraffLibAPI.database.entities.user.user_entity import UserEntity
from GraffLibAPI.models.enums.role_type import RoleType
from GraffLibAPI.models.user_model import UserModel

def is_admin(user : UserEntity) -> bool:
    return user.role == RoleType.ADMIN

def is_admin(user : UserModel) -> bool:
    return user.role == RoleType.ADMIN
