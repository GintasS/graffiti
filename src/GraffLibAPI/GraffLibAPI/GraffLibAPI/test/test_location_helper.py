from decimal import *
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geoalchemy2.shape import to_shape
from GraffLibAPI.configuration.constants import *
import pytest
import GraffLibAPI.utils.location_helper as LocationHelperClass

def test_get_short_address():
    test_address = {
        "road": "1",
        "house_number": "2",
        "city": "3",
        "country": "4"
        }
    result_adress = LocationHelperClass.get_short_address(test_address)
    assert result_adress == "12, 3, 4"

def test_dms_to_dd():
    result_dd = LocationHelperClass.dms_to_dd((11.0, 60.0, 3600.0), 'E')
    assert result_dd == 13.0

def test_get_distance_between_two_coordinates():
    test_distance = 1317.7554645657162
    result_distance = LocationHelperClass.get_distance_between_two_coordinates((22.5726, 88.3639), (28.7041, 77.1025))
    assert result_distance == test_distance