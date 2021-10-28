from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.configuration.constants import *

def create_image_unique_url(unique_image_name : str, user_id : int, extension : str) -> str:
    return "http://localhost:8000/markers/"

def create_image_entities(image_metadata_model_object : ImageMetadataModel, image_location_model_object : ImageLocationModel, user_image_request : CreateUserImageRequest, unique_image_name : str, image_url : str):
    new_image = to_image_entity(user_image_request, unique_image_name, image_url)
    session.add(new_image)
    session.commit()
    
    image_metadata_entity = to_image_metadata_entity(image_metadata_model_object, unique_image_name)
    session.add(image_metadata_entity)
    session.commit()

    image_location_entity = to_image_location_entity(image_location_model_object.coordinates, image_metadata_entity.id)
    session.add(image_location_entity)
    session.commit()

    image_classification_entity = to_image_classification_entity(user_image_request.image_classification_model, unique_image_name)
    session.add(image_classification_entity)
    session.commit()

def is_image_has_correct_extension(extension) -> bool:
    return extension in IMAGE_ALLOWED_EXTENSIONS

def is_http_request_mime_type(mime_type) -> bool:
    return mime_type in HTTP_REQUEST_MIME_TYPES

def dms_to_dd(gps_coords, gps_coords_ref):
    d, m, s =  gps_coords
    dd = d + m / 60 + s / 3600
    if gps_coords_ref.upper() in ('S', 'W'):
        return -dd
    elif gps_coords_ref.upper() in ('N', 'E'):
        return dd
    else:
        raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))