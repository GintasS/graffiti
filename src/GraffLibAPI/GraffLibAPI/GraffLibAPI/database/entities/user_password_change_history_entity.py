import sqlalchemy as sa
import enum
from enum import Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Table, Column, ForeignKey
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.RoleType import RoleType
from GraffLibAPI.database.base import Base

class UserPasswordChangeHistoryEntity(Base):
    __tablename__ = "user_password_change_history"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, ForeignKey('user.id'))
    password_changed_at = sa.Column(sa.DATETIME)

class UserPasswordChangeHistoryEntitySchema(SQLAlchemySchema):
    class Meta:
        model = UserPasswordChangeHistoryEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    user_id = auto_field()
    password_changed_at = auto_field()