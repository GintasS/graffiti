from GraffLibAPI.configuration.constants import *
import requests

def is_virus(file):   
    headers = {
        'X-ApplicationID': VirusScan.APP_ID,
        'X-SecretKey': VirusScan.APP_SECRET
    }
    data = {
        'async': 'false',
    }
    files = {
        'inputFile': ("file", file)
    }
    response = requests.post(url=VirusScan.APP_URL, data=data, headers=headers, files=files)

    return ("File is clean" in response.text) != True