import requests
from GraffLibAPI.configuration.constants import *

def create_on_water_api_request(latitude, longitude):
    url = OnWaterApi.get_replaced_api_url(latitude, longitude)
    x = requests.get(url)

    if x is not None:
        return x.text
    else:
        return None

