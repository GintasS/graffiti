from flask import Blueprint, render_template, request

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_users = Blueprint('api-users', __name__, url_prefix='/v1/users')

@blueprint_users.route('', methods=['POST'])
def createUser():
    return {
        'message': 'This POST12 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password-recovery', methods=['PATCH'])
def sendPasswordRecoveryEmail():
    return {
        'message': 'This PATCH13 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password', methods=['PATCH'])
def updateUserPasswordAfterRecoveryEmail():
    return {
        'message': 'This PATCH14 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_users.route('/password', methods=['PUT'])
def updateUserPasswordUserIsAuthenticated():
    return {
        'message': 'This PUT15 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }
