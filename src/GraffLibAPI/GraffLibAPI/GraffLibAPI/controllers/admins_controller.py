from flask import Blueprint, request
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.models.requests.create_user_request import CreateUserRequest, CreateUserRequestSchema
from GraffLibAPI.database.entities.user_entity import UserEntity, UserEntitySchema

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_admins = Blueprint('api-admins', __name__, url_prefix='/v1')

@blueprint_admins.route('/admins/users', methods=['GET'])
def get_users():
    try:
        users = session.query(UserEntity).all()
        user_entity_schema = UserEntitySchema(many=True)
    except:
        return "Internal server errror.", 500

    return {
        'message': 'This PATCH13 endpoint should update the entity',
        'method': request.method,
        'body': user_entity_schema.dump(users)
    }

@blueprint_admins.route('/users/<int:user_id>/', methods=['GET'])
def get_specific_user(user_id):
    return {
        'message': 'This GET2 SPECIFIC endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }

@blueprint_admins.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_specific_user(user_id):
    return {
        'message': 'This DELETE3 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }


@blueprint_admins.route('/users/<int:user_id>/images/<int:image_id>', methods=['DELETE'])
def delete_specific_image_for_user(user_id, image_id):
    return {
        'message': 'This endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id,
        'imageId': image_id
    }
