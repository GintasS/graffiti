# Library imports.
from flask import Blueprint, render_template, request, jsonify
from secrets import token_urlsafe
import requests
import io
import json
import datetime
from PIL import Image
from exif import Image as Img
import os
import os.path as pathh
from pathlib import Path
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError

class VirusScan():
    def __init__(self, response):
        self.response = response
    def virus_scanning(a, directory, unique_image_name, file_extension):
        endpoint = "https://api.virusscannerapi.com/virusscan"
        headers = {
            'X-ApplicationID': '36af45c9-f7bf-4928-b319-dfc2cb7a5e6f',
            'X-SecretKey': '0fe6ce8a-9fca-42ba-83fb-b12e72258b1c'
        }
        image_file_path = os.path.join(directory, unique_image_name + "." + file_extension)
        file = open(image_file_path, errors="ignore")
        data = {
            'async': 'false',
        }
        files = {
            'inputFile': (image_file_path, file.read())
        }
        r = requests.post(url=endpoint, data=data, headers=headers, files = files)
        a.response = r.text

