from decimal import *
from geopy.geocoders import Nominatim

def get_address_from_coordinates(latitude : Decimal, longitude : Decimal) -> str:
    geolocator = Nominatim(user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
    location = geolocator.reverse(str(latitude) + ", " + str(longitude))
    return location.address
