# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column, ForeignKey
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base
from GraffLibAPI.models.enums.marker_status import MarkerStatus

class MarkerMetadataEntity(Base):
    __tablename__ = "marker_metadata"

    id = sa.Column(sa.Integer, primary_key=True)
    marker_id = sa.Column(sa.String, ForeignKey('marker.id'), nullable=False)
    created_at = sa.Column(sa.TIMESTAMP, nullable=False)
    last_update = sa.Column(sa.TIMESTAMP, nullable=False)
    children = relationship("MarkerLocationEntity")


class MarkerMetadataEntitySchema(SQLAlchemySchema):
    class Meta:
        model = MarkerMetadataEntity
        load_instance = True  # Optional: deserialize to model instances
    
    id = auto_field()
    marker_id = auto_field()
    created_at = auto_field()
    last_update = auto_field()