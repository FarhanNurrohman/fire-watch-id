import requests

def fetch_weather(latitude:float, longitude:float) ->dict :
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : latitude,
        "longitude":longitude,
        "current":[
            "temperature2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "wind_direction_10m"
        ],
        "timezone":"Jakarta"
    }
    response = requests(url, params=params, timeout=15)
    response.raise_for_status()

    return response.json()

def parse_weather(data:dict)->dict:
    current_data = data["current"]
    return {
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "temperature": current_data["temperature_2m"],
        "humidity": current_data["relative_humidity_2m"],
        "precipitation":current_data["precipitation"],
        "wind_speed": current_data["wind_speed_10m"],
        "weather_code": current_data["weather_code"]
    }