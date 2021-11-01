# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base

class ImageMetadataEntity(Base):
    __tablename__ = "image_metadata"

    id = sa.Column(sa.Integer, primary_key=True)
    image_unique_name = sa.Column(sa.String, ForeignKey('image.image_unique_name'), nullable=False)
    original_image_name = sa.Column(sa.String, nullable=False)
    extension =  sa.Column(sa.String(ImageValidation.IMAGE_EXTENSION_MAX_LENGTH), nullable=False)
    photographed_time = sa.Column(sa.TIMESTAMP, nullable=False)
    upload_time = sa.Column(sa.TIMESTAMP, nullable=False)
    children = relationship("ImageLocationEntity")

class ImageMetadataEntitySchema(SQLAlchemySchema):
    class Meta:
        model = ImageMetadataEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    image_unique_name = auto_field()
    original_image_name = auto_field()
    extension = auto_field()
    photographed_time = auto_field()
    upload_time = auto_field()