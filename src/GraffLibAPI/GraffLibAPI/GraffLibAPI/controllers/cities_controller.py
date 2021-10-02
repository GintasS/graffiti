from flask import Blueprint, render_template, request

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_cities = Blueprint('api-cities', __name__, url_prefix='/v1/cities')

@blueprint_cities.route('', methods=['GET'])
def get_city():
    return {
        'message': 'This GET4 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }

@blueprint_cities.route('', methods=['POST'])
def create_city():
    return {
        'message': 'This POST5 endpoint should update the entity',
        'method': request.method,
        'body': request.json
    }
