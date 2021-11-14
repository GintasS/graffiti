from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus
from GraffLibAPI.models.responses.create_marker_image_response import CreateMarkerImageResponse, CreateMarkerImageResponseSchema

def create_image_unique_url(unique_image_name : str, marker_id : str, extension : str) -> str:
    return Application.APP_URL + "/static/markers/" + marker_id + "/" + unique_image_name + "." + extension

def is_image_has_correct_extension(extension) -> bool:
    return extension in ImageValidation.IMAGE_ALLOWED_EXTENSIONS

def is_http_request_mime_type(mime_type) -> bool:
    return mime_type in ImageValidation.HTTP_REQUEST_MIME_TYPES