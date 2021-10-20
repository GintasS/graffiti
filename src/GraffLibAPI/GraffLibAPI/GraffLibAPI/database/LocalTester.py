import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
import os
engine = sa.create_engine("sqlite:///" + os.path.abspath("src/GraffLibAPI/GraffLibAPI/GraffLibAPI/database/main-db.db"))
session = scoped_session(sessionmaker(bind=engine))

print(list(session)