import requests
import json

import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')
print(f'Ваш API ключ: {api_key}')


# lan and lon of Korsnas (It was rainy)
def GetLocationKey(lat = 62.65, lon = 20.18):
    # Get location key by (lat, lon)

    url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
    params = {
        'apikey': api_key,
        'q': ','.join([str(lat), str(lon)])
    }
    response = requests.get(url, params=params)

    location_key = None
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))
        location_key = data['Key']
    else:
        print(f'Error: {response.status_code}')
    
    return location_key


def GetWeatherData(location_key):
    # Get weather information by location key

    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
    params = {
        'apikey': api_key,
        'details': 'true'
    }

    response = requests.get(url, params=params)
    data = None
    if response.status_code == 200:
        data = response.json()[0]
        print(json.dumps(data, indent=4, ensure_ascii=False))
        print(data)
    else:
        print(f'Error: {response.status_code}')
    
    return data


data = None
location_key = GetLocationKey()

if location_key:
    data = GetWeatherData(location_key)

temp, hum, wind_speed = None, None, None
if data:
    #Parse temperature humidity and wind's speed
    temp = data['Temperature']['Metric']['Value']
    hum = data['RelativeHumidity']
    wind_speed = data['Wind']['Speed']['Metric']['Value']
