# Library imports.
import json
from flask import Blueprint, render_template, request, jsonify
from marshmallow import ValidationError

# Project imports.
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.database.entities.user.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.utils.user_helper import *

from GraffLibAPI.database.entities.user.user_password_reset_entity import *
from GraffLibAPI.database.entities.user.user_password_reset_history_entity import *
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.database.entities.image.image_entity import ImageEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModel, ImageClassificationModelSchema
from GraffLibAPI.database.entities.marker.marker_entity import MarkerEntity
from GraffLibAPI.database.entities.marker.marker_location_entity import MarkerLocationEntity
from GraffLibAPI.database.entities.marker.marker_metadata_entity import MarkerMetadataEntity

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_admins = Blueprint("api-admins", __name__, url_prefix="/v1")

@blueprint_admins.route("/users", methods=["GET"])
def get_users():
    try:
        users = session.query(UserEntity).all()

        return { "body": UserEntitySchema(many=True).dump(users) }, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500

@blueprint_admins.route("/users/<int:user_id>/", methods=["GET"])
def get_specific_user(user_id):
    try:
        found_user = session.query(UserEntity).filter(UserEntity.id == user_id).first()

        if found_user is None:
            return "User does not exist", 404

        return { "body": UserEntitySchema().dump(found_user) }, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error.", 500

@blueprint_admins.route("/users/<int:user_id>/", methods=["DELETE"])
def delete_specific_user(user_id):
    try:
        found_user = session.query(UserEntity).filter(UserEntity.id == user_id).first()
        
        if found_user is None:
            return "User does not exist", 404
        if is_admin(found_user) is True:
            return "User of type Administrator can't be deleted.", 409

        user_join = session.query(
                 UserPasswordResetEntity, UserPasswordResetHistoryEntity
            ).filter(
                 UserPasswordResetEntity.user_id == found_user.id
            ).filter(
                 UserPasswordResetHistoryEntity.reset_id == UserPasswordResetEntity.id
            ).all()

        image_join = session.query(
                ImageEntity
            ).filter(
                ImageEntity.user_id == user_id
            ).all()

        marker_join = session.query(
                MarkerEntity
            ).all()

        # TODO: [AUDIT] If user deletes his/her account, we will not know who created images.
        for img in image_join:
            img.user_id = None
            session.commit()

        for mrk in marker_join:
            mrk.user_id = None
            session.commit()

        for user in user_join:
            session.delete(user[1])
            session.delete(user[0])
            session.commit()

        session.delete(found_user)
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server error." , 500