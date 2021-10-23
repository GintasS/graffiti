# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.RoleType import RoleType
from GraffLibAPI.database.base import Base
from GraffLibAPI.models.enums.user_password_reset_type import UserPasswordResetType

class UserPasswordResetEntity(Base):
    __tablename__ = "user_password_reset"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, ForeignKey('user.id'))
    reset_type = sa.Column(sa.Enum(UserPasswordResetType), nullable=False)
    token = sa.Column(sa.String, nullable=False)
    children = relationship("UserPasswordResetHistoryEntity")

class UserPasswordResetEntitySchema(SQLAlchemySchema):
    class Meta:
        model = UserPasswordResetEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    user_id = auto_field()
    reset_type = auto_field()
    token = auto_field()
