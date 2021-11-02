# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus

class ImageEntity(Base):
    __tablename__ = "image"

    # TODO: [REFACTORING] Rename image_unique_name to id.
    image_unique_name = sa.Column(sa.String, primary_key=True)
    marker_id = sa.Column(sa.String, ForeignKey('marker.id'), nullable=False)
    user_id = sa.Column(sa.Integer, ForeignKey('user.id'), nullable=True)
    graffiti_status = sa.Column(sa.Enum(GraffitiStatus), nullable=False)
    children = relationship("ImageMetadataEntity")
    children2 = relationship("ImageClassificationEntity")


class ImageEntitySchema(SQLAlchemySchema):
    class Meta:
        model = ImageEntity
        load_instance = True  # O ptional: deserialize to model instances

    image_unique_name = auto_field()
    marker_id = auto_field()
    user_id = auto_field()
    graffiti_status = auto_field()