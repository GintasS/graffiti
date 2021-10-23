# Library includes.
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import UniqueConstraint, CheckConstraint, Table, Column
from sqlalchemy.orm import relationship

# Project includes.
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.RoleType import RoleType
from GraffLibAPI.database.base import Base

# TODO: some of the relationships may be one-to-many, but we want to enforce(at least make ORM expect) one-to-one relationships.

class UserEntity(Base):
    __tablename__ = "user"
    __table_args__ = (
            UniqueConstraint('user_name'),
            UniqueConstraint('email'),
            CheckConstraint(f'length(user_name) >= {USERNAME_MIN_LENGTH} AND length(user_name) <= {USERNAME_MAX_LENGTH}', name='check_username_length'),
            CheckConstraint(f'length(email) >= {EMAIL_MIN_LENGTH} AND length(email) <= {EMAIL_MAX_LENGTH}', name='check_email_length'),
            CheckConstraint(f'length(password) >= {PASSWORD_MIN_LENGTH} AND length(password) <= {PASSWORD_MAX_LENGTH}', name='check_password_length'),

            # Not checking here for valid email and role, this will be done on API layer.
            # TODO: Remove constraints.
            )

    # TODO: Add validation for all columns for all entities.
    # TODO: Add validation for all fields in models.

    id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String(USERNAME_MAX_LENGTH), nullable=False)
    first_name = sa.Column(sa.Unicode, nullable=False)
    last_name = sa.Column(sa.Unicode, nullable=False)
    email = sa.Column(sa.String(EMAIL_MAX_LENGTH), nullable=False)
    password = sa.Column(sa.String(PASSWORD_MAX_LENGTH), nullable=False)
    role = sa.Column(sa.Enum(RoleType), nullable=False)
    created_at = sa.Column(sa.TIMESTAMP)
    children = relationship("UserPasswordResetEntity")
    children2 = relationship("ImageEntity")

class UserEntitySchema(SQLAlchemySchema):
    class Meta:
        model = UserEntity
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    user_name = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    email = auto_field()
    password = auto_field()
    role = auto_field()
    created_at = auto_field()