# Library imports.
from flask import Blueprint, render_template, request, jsonify
from secrets import token_urlsafe
import json
import datetime
from PIL import Image
from exif import Image as Img
import os
import os.path as pathh
from pathlib import Path
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError
import logging
logger = logging.getLogger()

from GraffLibAPI.database.db_setup import session
from GraffLibAPI.utils import compare_image_helper
from GraffLibAPI.models.responses.compare_two_images_response import CompareTwoImagesResponse, CompareTwoImagesResponseSchema
from GraffLibAPI.database.entities.image.image_entity import ImageEntity
from GraffLibAPI.database.entities.image.image_metadata_entity import ImageMetadataEntity
from GraffLibAPI.database.entities.image.image_location_entity import ImageLocationEntity
from GraffLibAPI.database.entities.image.image_classification_entity import ImageClassificationEntity
from GraffLibAPI.utils.file_helper import *
from GraffLibAPI.utils.image_helper import *
from GraffLibAPI.utils.datetime_parser import *
from GraffLibAPI.utils.location_helper import *

blueprint_image_comparison = Blueprint("api-image-comparison", __name__, url_prefix="/v1")

@blueprint_image_comparison.route("/images/<string:image_id_to_compare>/<string:image_id_to_compare_against>/comparison", methods=["GET"])
def compare_two_images(image_id_to_compare, image_id_to_compare_against):
    image_to_compare = session.query(ImageEntity).\
        filter(
            ImageEntity.image_unique_name == image_id_to_compare
        ).\
        first()

    image_to_compare_against = session.query(ImageEntity).\
        filter(
            ImageEntity.image_unique_name == image_id_to_compare_against
        ).\
        first()

    logger.warning("After SQL queries.")
    if image_to_compare is None:
        return "Image to compare was not found.", 404
    if image_to_compare_against is None:
        return "Image to compare against was not found.", 404
    if image_id_to_compare == image_id_to_compare_against:
        return "Images must be different.", 409

    logger.warning("After IF statements.")
    directory_image_to_compare = get_current_directory(image_to_compare.marker_id)
    directory_image_to_compare_against = get_current_directory(image_to_compare_against.marker_id)

    logger.warning("After fetching dir.")

    image_to_compare_file_path = get_image_full_path(directory_image_to_compare, image_to_compare.image_unique_name, "jpeg")
    image_to_compare_against_file_path = get_image_full_path(directory_image_to_compare_against, image_to_compare_against.image_unique_name, "jpeg")
    
    logger.warning("After Getting Image path.")
    index = compare_image_helper.compare_two_images(image_to_compare_file_path, image_to_compare_against_file_path)
    logger.warning("After calculating similarity index.")

    response = CompareTwoImagesResponse(index)

    return { "body": CompareTwoImagesResponseSchema().dump(response) }, 200