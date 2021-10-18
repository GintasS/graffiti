# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from marshmallow_geojson import GeoJSONSchema, PropertiesSchema, FeatureSchema

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.RoleType import RoleType
from GraffLibAPI.database.base import Base

class ImageLocationEntity(Base):
    __tablename__ = "image_location"

    id = sa.Column(sa.Integer, ForeignKey('image_metadata.id'), primary_key=True)
    coordinates = sa.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

class ImageLocationEntitySchema(GeoJSONSchema):
    class Meta:
        model = ImageLocationEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    coordinates = auto_field()