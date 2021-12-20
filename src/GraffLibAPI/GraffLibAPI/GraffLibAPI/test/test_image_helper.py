from urllib.parse import urljoin
import pytest
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus
from GraffLibAPI.models.responses.create_marker_image_response import CreateMarkerImageResponse, CreateMarkerImageResponseSchema
import GraffLibAPI.utils.image_helper as ImageHelperClass

def test_create_image_unique_url():
    test_url = urljoin(Application.APP_URL, "static/markers/1/2.png")
    result_url = ImageHelperClass.create_image_unique_url("1", "2", "png")
    assert result_url == test_url

def test_is_image_has_correct_extension_true():
    test_extension = "png"
    result_extension = ImageHelperClass.is_image_has_correct_extension(test_extension)
    assert result_extension == True

def test_is_image_has_correct_extension_false():
    test_extension = "gif"
    result_extension = ImageHelperClass.is_image_has_correct_extension(test_extension)
    assert result_extension == False

def test_is_http_request_mime_type_true():
    test_mime_type = "image/png"
    result_mime_type = ImageHelperClass.is_http_request_mime_type(test_mime_type)
    assert result_mime_type == True

def test_is_http_request_mime_type_false():
    test_mime_type = "video/gif"
    result_mime_type = ImageHelperClass.is_http_request_mime_type(test_mime_type)
    assert result_mime_type == False
