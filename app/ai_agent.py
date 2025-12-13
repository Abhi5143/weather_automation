def generate_weather_summary(city: str, temperature: float, description: str) -> str:
    return f"Weather Update for {city}: Temperature: {temperature}°C Condition: {description.capitalize()}. Advice: Stay safe and plan accordingly."
