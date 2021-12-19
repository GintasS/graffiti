"""
This script runs the GraffLibAPI application using a development server.
"""

from gevent.pywsgi import WSGIServer
from os import environ
from GraffLibAPI import app

# TODO: [PYTHON] Update project to use newest python version and newest packages.
# TODO: [EMAIL] After user signs up, we need a confirmation email logic.

http_server = WSGIServer(('0.0.0.0', 8000), app)
http_server.serve_forever()
