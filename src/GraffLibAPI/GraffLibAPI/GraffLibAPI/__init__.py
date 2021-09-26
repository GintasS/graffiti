"""
The flask application package.
"""

from flask import Flask
from GraffLibAPI.controllers.imagescontroller import blueprint_users as user_endpoints
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

# Register our created blueprints.
app.register_blueprint(user_endpoints)

### swagger specific ###
SWAGGER_URL = '/swagger'
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
import GraffLibAPI.controllers.citycontroller
import GraffLibAPI.controllers.imagescontroller
import GraffLibAPI.controllers.markerscontroller
import GraffLibAPI.controllers.userscontroller
import GraffLibAPI.controllers.imagescontroller