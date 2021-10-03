import json
from flask import Blueprint, render_template, request, jsonify
from GraffLibAPI.models.enums import RoleType
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.models.responses.create_user_response import CreateUserResponse, CreateUserResponseSchema
from GraffLibAPI.models.user_model import UserModel
from GraffLibAPI.database.entities.user_entity import UserEntity, UserEntitySchema
from GraffLibAPI.database.db_setup import session
from marshmallow import ValidationError
from linq import Flow
import datetime as dt
from GraffLibAPI.mappings.mappings import *

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
    return {
        'message': 'This PATCH13 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password', methods=['PATCH'])
def update_user_password_after_recovery_email():
    return {
        'message': 'This PATCH14 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password', methods=['PUT'])
def update_user_password_user_is_authenticated():
    return {
        'message': 'This PUT15 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }
