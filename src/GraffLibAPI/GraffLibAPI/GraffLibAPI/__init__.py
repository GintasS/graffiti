"""
The flask application package.
"""

from flask import Flask

from flask_swagger_ui import get_swaggerui_blueprint

from GraffLibAPI.controllers.admins_controller import blueprint_admins as admin_endpoints
from GraffLibAPI.controllers.cities_controller import blueprint_cities as city_endpoints
from GraffLibAPI.controllers.images_controller import blueprint_images as image_endpoints
from GraffLibAPI.controllers.markers_controller import blueprint_markers as marker_endpoints
from GraffLibAPI.controllers.users_controller import blueprint_users as user_endpoints

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

# Register our created blueprints.
app.register_blueprint(admin_endpoints)
app.register_blueprint(city_endpoints)
app.register_blueprint(image_endpoints)
app.register_blueprint(marker_endpoints)
app.register_blueprint(user_endpoints)

### swagger specific ###
SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "GraffLib REST API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###
