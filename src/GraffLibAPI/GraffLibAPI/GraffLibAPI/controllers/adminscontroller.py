from flask import Blueprint, render_template, request

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_admins = Blueprint('api-admins', __name__, url_prefix='/v1')

@blueprint_admins.route('/admins/users', methods=['GET'])
def getAllUsers():
    return {
        'message': 'This GET1 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_admins.route('/users/<int:user_id>/', methods=['GET'])
def getSpecificUser(user_id):
    return {
        'message': 'This GET2 SPECIFIC endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }

@blueprint_admins.route('/users/<int:user_id>/', methods=['DELETE'])
def deleteSpecificUser(user_id):
    return {
        'message': 'This DELETE3 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }


@blueprint_admins.route('/users/<int:user_id>/images/<int:image_id>', methods=['DELETE'])
def deleteSpecificImageForUser(user_id, image_id):
    return {
        'message': 'This endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id,
        'imageId': image_id
    }
