from flask import Blueprint, render_template, request

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_images = Blueprint('api-images', __name__, url_prefix='/v1/users')

@blueprint_images.route('/<int:user_id>/images', methods=['GET'])
def getUserImage(user_id):
    return {
        'message': 'This GET6 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }

@blueprint_images.route('/<int:user_id>/images', methods=['POST'])
def createUserImage(user_id):
    return {
        'message': 'This POST7 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'userId': user_id
    }