import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        raise ValueError(f"Could not get weather data for {city}: {data.get('message', 'Unknown error')}")

    return {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
