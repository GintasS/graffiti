"""
This script runs the GraffLibAPI application using a development server.
"""

from os import environ
from GraffLibAPI import app

# TODO: [PRODUCTION] Do not use DEV build for PROD.
# TODO: [PYTHON] Update project to use newest python version and newest packages.

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)
