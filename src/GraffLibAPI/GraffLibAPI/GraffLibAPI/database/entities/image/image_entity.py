# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.RoleType import RoleType
from GraffLibAPI.database.base import Base

class ImageEntity(Base):
    __tablename__ = "image"

    image_unique_name = sa.Column(sa.String, nullable=False, primary_key=True)
    user_id = sa.Column(sa.Integer, ForeignKey('user.id'))
    children = relationship("ImageMetadataEntity")
    children2 = relationship("ImageClassificationEntity")


class ImageEntitySchema(SQLAlchemySchema):
    class Meta:
        model = ImageEntity
        load_instance = True  # Optional: deserialize to model instances

    image_unique_name = auto_field()
    user_id = auto_field()