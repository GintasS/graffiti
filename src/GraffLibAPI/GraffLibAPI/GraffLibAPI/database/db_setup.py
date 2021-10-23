# Library includes.
import sqlalchemy as sa
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.event import listen

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.database.base import Base

#
#
# Registering Databse entities.
#
#

# !!! Order of these imports matter !!!
# Children should come first, before the parent.
from GraffLibAPI.database.entities.user_password_reset_history_entity import UserPasswordResetHistoryEntity
from GraffLibAPI.database.entities.user_password_reset_entity import UserPasswordResetEntity

from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.database.entities.image.image_entity import ImageEntity

from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.database.entities.city_entity import CityEntity

engine = sa.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine, checkfirst=True)