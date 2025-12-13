from .email_service import send_email

def check_and_alert(city: str, temperature: float, description: str):
    # Example alert conditions
    if "rain" in description.lower() or temperature > 35:
        subject = f"Weather Alert for {city}"
        content = f"Weather alert for {city}!\nTemperature: {temperature}°C\nCondition: {description}"
        send_email(subject, content)
