import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from GraffLibAPI.configuration.constants import SQLALCHEMY_DATABASE_URI

from GraffLibAPI.database.base import Base

# Order of these imports matter!!!
from GraffLibAPI.database.entities.user_password_reset_history_entity import UserPasswordResetHistoryEntity
from GraffLibAPI.database.entities.user_password_reset_entity import UserPasswordResetEntity
from GraffLibAPI.database.entities.user_entity import UserEntity
from GraffLibAPI.database.entities.city_entity import CityEntity




engine = sa.create_engine(SQLALCHEMY_DATABASE_URI)
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine, checkfirst=True)
