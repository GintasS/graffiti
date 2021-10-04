# Library imports
import json
from flask import Blueprint, render_template, request, jsonify
from linq import Flow
import datetime as dt
from sqlalchemy import update
from marshmallow import ValidationError

# Project imports
from GraffLibAPI.models.enums import RoleType
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.models.responses.create_user_response import CreateUserResponse, CreateUserResponseSchema
from GraffLibAPI.models.user_model import UserModel
from GraffLibAPI.database.entities.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.models.requests.update_authenticated_user_password_request import UpdateAuthenticatedUserPasswordRequest, UpdateAuthenticatedUserPasswordRequestSchema
from GraffLibAPI.database.entities.user_password_change_history_entity import UserPasswordChangeHistoryEntity, UserPasswordChangeHistoryEntitySchema
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.utils.email_sender_helper import send_email, create_password_recovery_email
from GraffLibAPI.models.requests.send_password_recovery_email_request import SendPasswordRecoveryEmailRequest, SendPasswordRecoveryEmailRequestSchema

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_users = Blueprint('api-users', __name__, url_prefix='/v1/users')

@blueprint_users.route('', methods=['POST'])
def create_user():
    try:
        create_user_request = CreateUserRequestSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500
    
    if Flow(session.query(UserEntity).all()).Any(lambda x: x.user_name == create_user_request.user_name or 
                       x.email == create_user_request.email).stream == True:
        return "User already exists", 409

    new_user = from_create_user_request_to_user_entity(create_user_request)
    user_schema = UserEntitySchema()
    session.add(new_user)
    session.commit()

    return from_user_entity_to_create_user_response(new_user).toJSON(), 201

@blueprint_users.route('/password-recovery', methods=['PATCH'])
def send_password_recovery_email():
    try:
        send_password_recovery_email_request = SendPasswordRecoveryEmailRequestSchema().load(request.get_json())

        email_message = create_password_recovery_email(send_password_recovery_email_request.email)
        send_email(email_message)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

    return "", 204

@blueprint_users.route('/password', methods=['PATCH'])
def update_user_password_after_recovery_email():
    return {
        'message': 'This PATCH14 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password', methods=['PUT'])
def update_user_password_user_is_authenticated():
    try:
        update_authenticated_user_password_request = UpdateAuthenticatedUserPasswordRequestSchema().load(request.get_json())
        
        # TODO: check if the you're changing password for the same user who is authenticated.
        # If not, return 422.
        # TODO: don't forget to hash passwords on the client and then send to the API due to security.

        target_user = session.query(UserEntity).filter_by(id=update_authenticated_user_password_request.user_id).first()

        # TODO: check if the user password changing algorithm is secure, we are not missing something.
        if target_user is None:
            return "User was not found.", 404
        if target_user.password != update_authenticated_user_password_request.old_password:
            return "The old password is incorrect.", 409
        if  target_user.password == update_authenticated_user_password_request.new_password:
            return "The new password and the old password should not be the same.", 409

        target_user.password = update_authenticated_user_password_request.new_password
        user_password_change_history_entity = from_user_entity_to_user_password_change_history_entity(target_user)

        session.add(user_password_change_history_entity)
        session.commit()

    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500

    return "", 204
