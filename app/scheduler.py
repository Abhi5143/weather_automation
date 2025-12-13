import schedule
import time
from .weather_service import get_weather
from .alert_service import check_and_alert

CITIES = ["London", "Mumbai", "New York"]  # List of cities to monitor

def job():
    for city in CITIES:
        data = get_weather(city)
        print(f"Checking weather for {city}: {data}")
        check_and_alert(city, data["temperature"], data["description"])

# Run the job every 1 hour
schedule.every(1).hours.do(job)

print("Weather automation scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(10)
