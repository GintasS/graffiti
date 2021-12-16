from decimal import *
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geoalchemy2.shape import to_shape
from GraffLibAPI.configuration.constants import *

def get_location_from_coordinates(latitude : Decimal, longitude : Decimal) -> str:
    geolocator = Nominatim(user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    location = geolocator.reverse(str(latitude) + ", " + str(longitude), language='en', addressdetails=True)

    if location is None:
        return None
    else:
        return location
def parse_address(address : dict) -> str:
    # TODO: [REFACTORING] This will limit markers to city boundaries only. Refactor this (and endpoints) to include rural areas.
    if address.get("road") is None or\
       address.get("country") is None or\
       (address.get("city") is None and\
        address.get("town") is None):
        return None

    parsed_address = {
        "road": address.get("road"),
        "house_number": address.get("house_number"),
        "city": address.get("town") if address.get("city") is None else address.get("city"),
        "country": address.get("country"),
    }

    parsed_address["full_address"] = parsed_address["road"] + " " + parsed_address["house_number"] + ", " + parsed_address["city"] + ", " + parsed_address["country"]
    return parsed_address

def dms_to_dd(gps_coords, gps_coords_ref):
    d, m, s =  gps_coords
    dd = d + m / 60 + s / 3600
    if gps_coords_ref.upper() in ('S', 'W'):
        return -dd
    elif gps_coords_ref.upper() in ('N', 'E'):
        return dd
    else:
        raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))

def get_distance_between_two_coordinates(coords_1, coords_2):
    return great_circle(coords_1, coords_2).km

def is_new_marker_too_close_to_existing_one(markers_join, new_marker_coordinates) -> bool:
    marker_distances  = []
    for mrk in markers_join:
        mrk_parsed_coordinates = to_shape(mrk[0].coordinates)
        mrk_coordinates_list = [ mrk_parsed_coordinates.x, mrk_parsed_coordinates.y ]

        distance_from_this_new_marker_to_mrk = get_distance_between_two_coordinates(mrk_coordinates_list, new_marker_coordinates)
        marker_distances.append(distance_from_this_new_marker_to_mrk)

    near_markers_count = 0
    for distance in marker_distances:
        if distance <= LocationValidation.NEW_MARKER_MIN_DISTANCE_BETWEEN_EXISTING_MARKER:
            return True

    return False