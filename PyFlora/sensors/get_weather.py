import requests
import os
import creds

url = creds.url
api_key = creds.OWM_API_KEY
city = creds.OWM_CITY


def get_weather_data():

    r = requests.get(url=url, params=
            {
                'q':city,
                'appid':api_key
                
            },
            ).json()
    
    humidity = r['main']['humidity']
    description = r['weather'][0]['description']
    temp = str(r['main']['temp']) + " C°"
    precise_location = r['name']

    return humidity, description, temp, precise_location
