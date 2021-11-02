# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base

class MarkerLocationEntity(Base):
    __tablename__ = "marker_location"

    id = sa.Column(sa.Integer, ForeignKey('marker_metadata.id'), primary_key=True)
    country = sa.Column(sa.Unicode(LocationValidation.COUNTRY_NAME_MAX_LENGTH), nullable=False)
    city = sa.Column(sa.Unicode(LocationValidation.CITY_NAME_MAX_LENGTH), nullable=False)
    address = sa.Column(sa.Unicode(LocationValidation.STREET_ADDRESS_MAX_LENGTH), nullable=False)
    coordinates = sa.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

class MarkerLocationEntitySchema(GeoJSONSchema):
    class Meta:
        model = MarkerLocationEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    country = auto_field()
    city = auto_field()
    address = auto_field()
    coordinates = auto_field()