"""
The flask application package.
"""

from flask import Flask
from GraffLibAPI.controllers.userscontroller import blueprint_users as user_endpoints
from GraffLibAPI.controllers.adminscontroller import blueprint_admins as admin_endpoints
from GraffLibAPI.controllers.imagescontroller import blueprint_images as image_endpoints
from GraffLibAPI.controllers.markerscontroller import blueprint_markers as marker_endpoints
from GraffLibAPI.controllers.citiescontroller import blueprint_cities as city_endpoints

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

# Register our created blueprints.
app.register_blueprint(user_endpoints)
app.register_blueprint(admin_endpoints)
app.register_blueprint(image_endpoints)
app.register_blueprint(marker_endpoints)
app.register_blueprint(city_endpoints)

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

import GraffLibAPI.views
import GraffLibAPI.controllers.citiescontroller
import GraffLibAPI.controllers.imagescontroller
import GraffLibAPI.controllers.markerscontroller
import GraffLibAPI.controllers.userscontroller
import GraffLibAPI.controllers.imagescontroller
import GraffLibAPI.controllers.adminscontroller