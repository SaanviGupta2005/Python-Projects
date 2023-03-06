import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "60190400e0a6e7429e4cdb92d0374fd7"


weather_params = {"lat": 19.075983, "lon": 72.877655, "appid": api_key}

response = requests.get(OWN_ENDPOINT, params=weather_params)
print(response.json())
