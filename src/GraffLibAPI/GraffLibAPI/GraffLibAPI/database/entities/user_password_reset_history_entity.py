# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Table, Column, ForeignKey

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base

class UserPasswordResetHistoryEntity(Base):
    __tablename__ = "user_password_reset_history"

    id = sa.Column(sa.Integer, primary_key=True)
    reset_id = sa.Column(sa.Integer, ForeignKey('user_password_reset.id'))
    reset_iniatiated = sa.Column(sa.DATETIME)
    reset_completed = sa.Column(sa.DATETIME, nullable=True)


class UserPasswordResetHistoryEntitySchema(SQLAlchemySchema):
    class Meta:
        model = UserPasswordResetHistoryEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    reset_id = auto_field()
    reset_iniatiated = auto_field()
    reset_completed = auto_field()