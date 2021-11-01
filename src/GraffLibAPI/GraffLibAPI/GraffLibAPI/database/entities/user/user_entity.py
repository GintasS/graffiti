# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.role_type import RoleType
from GraffLibAPI.database.base import Base

# TODO: [DATABASE] Some of the relationships may be one-to-many, but we want to enforce(at least make ORM expect) one-to-one relationships.

class UserEntity(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String(UserValidation.USERNAME_MAX_LENGTH), nullable=False)
    first_name = sa.Column(sa.Unicode(UserValidation.FISRT_NAME_MAX_LENGTH), nullable=False)
    last_name = sa.Column(sa.Unicode(UserValidation.LAST_NAME_MAX_LENGTH), nullable=False)
    email = sa.Column(sa.String(UserValidation.EMAIL_MAX_LENGTH), nullable=False)
    password = sa.Column(sa.LargeBinary(UserValidation.PASSWORD_BINARY_FORM_MAX_LENGTH), nullable=False)
    role = sa.Column(sa.Enum(RoleType), nullable=False)
    created_at = sa.Column(sa.TIMESTAMP, nullable=False)
    children = relationship("UserPasswordResetEntity")
    children2 = relationship("ImageEntity")
    children3 = relationship("MarkerEntity")

class UserEntitySchema(SQLAlchemySchema):
    class Meta:
        model = UserEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    user_name = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    email = auto_field()
    password = auto_field()
    role = auto_field()
    created_at = auto_field()