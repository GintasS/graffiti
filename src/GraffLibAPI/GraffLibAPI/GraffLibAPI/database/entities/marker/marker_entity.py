# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base
from GraffLibAPI.models.enums.marker_status import MarkerStatus

class MarkerEntity(Base):
    __tablename__ = "marker"

    id = sa.Column(sa.String, nullable=False, primary_key=True)
    user_id = sa.Column(sa.Integer, ForeignKey('user.id'), nullable=True)
    marker_status = sa.Column(sa.Enum(MarkerStatus), nullable=False)
    children = relationship("MarkerMetadataEntity")

class MarkerEntitySchema(SQLAlchemySchema):
    class Meta:
        model = MarkerEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    user_id = auto_field()
    marker_status = auto_field()