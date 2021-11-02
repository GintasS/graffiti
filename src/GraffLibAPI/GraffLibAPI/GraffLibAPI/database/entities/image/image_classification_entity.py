# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.image_direction import ImageDirection
from GraffLibAPI.database.base import Base

class ImageClassificationEntity(Base):
    __tablename__ = "image_classification"

    image_unique_name = sa.Column(sa.String, ForeignKey('image.image_unique_name'), primary_key=True)
    user_provided_name = sa.Column(sa.Unicode(ImageValidation.USER_PROVIDED_IMAGE_NAME_MAX_LENGTH), nullable=True)
    description = sa.Column(sa.Unicode(ImageValidation.IMAGE_DESCRIPTION_MAX_LENGTH), nullable=True)
    graffiti_object = sa.Column(sa.Unicode(ImageValidation.IMAGE_DESCRIPTION_MAX_LENGTH), nullable=True)  # TODO: [REFACTORING] In the future, perhaps, graffiti_object could be an Enum?
    direction = sa.Column(sa.Enum(ImageDirection), nullable=True)

class ImageClassificationEntitySchema(SQLAlchemySchema):
    class Meta:
        model = ImageClassificationEntity
        load_instance = True  # Optional: deserialize to model instances

    image_unique_name = auto_field()
    user_provided_name = auto_field()
    description = auto_field()
    graffiti_object = auto_field()
    direction = auto_field()