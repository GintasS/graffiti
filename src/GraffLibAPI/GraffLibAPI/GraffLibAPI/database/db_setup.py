import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from GraffLibAPI.configuration.constants import SQLALCHEMY_DATABASE_URI

engine = sa.create_engine(SQLALCHEMY_DATABASE_URI)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()