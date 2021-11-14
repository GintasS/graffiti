"""
This script runs the GraffLibAPI application using a development server.
"""

from os import environ
from GraffLibAPI import app

# TODO: [PRODUCTION] Do not use DEV build for PROD.

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)
