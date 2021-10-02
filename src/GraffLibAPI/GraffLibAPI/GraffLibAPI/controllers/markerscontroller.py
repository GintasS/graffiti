from flask import Blueprint, render_template, request

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_markers = Blueprint('api-markers', __name__, url_prefix='/v1')

@blueprint_markers.route('/<string:city_name>/markers', methods=['GET'])
def getCityMarker(city_name):
    return {
        'message': 'This GET8 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'cityName': city_name
    }

@blueprint_markers.route('/<string:city_name>/markers', methods=['POST'])
def createCityMarker(city_name):
    return {
        'message': 'This POST9 endpoint should update the entity',
        'method': request.method,
        'body': request.json,
        'cityName': city_name
    }

@blueprint_markers.route('/markers/<int:marker_id>/images', methods=['GET'])
def getImagesForCityMarker(marker_id):
    return {
        'message': 'This GET232 should update the entity',
        'method': request.method,
        'body': request.json,
        'markerId': marker_id
    }


@blueprint_markers.route('/markers/<int:marker_id>/images', methods=['POST'])
def createImageForCityMarker(marker_id):
    return {
        'message': 'This POST11 should update the entity',
        'method': request.method,
        'body': request.json,
        'markerId': marker_id
    }