# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base

class CityEntity(Base):
    __tablename__ = "city"

    id = sa.Column(sa.Integer, primary_key=True)
    city_name = sa.Column(sa.Unicode(LocationValidation.CITY_NAME_MAX_LENGTH), nullable=False)

class CityEntitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CityEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    city_name = auto_field()