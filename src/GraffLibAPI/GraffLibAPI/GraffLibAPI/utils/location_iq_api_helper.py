from GraffLibAPI.configuration.constants import *
def create_location_iq_api_request(latitude, longitude):
    url = LocationIqApi.get_replaced_api_url(latitude, longitude)
    x = requests.get(url)

    if x is not None:
        return x.text
    else:
        return None