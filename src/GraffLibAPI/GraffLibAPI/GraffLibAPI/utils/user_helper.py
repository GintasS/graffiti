from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.models.enums import RoleType
from GraffLibAPI.models.user_model import UserModel

def is_admin(user : UserEntity) -> bool:
    return user.role == RoleType.RoleType.ADMIN

def is_admin(user : UserModel) -> bool:
    return user.role == RoleType.RoleType.ADMIN
