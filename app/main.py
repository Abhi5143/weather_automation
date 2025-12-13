from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import Base, engine, SessionLocal
from .models import WeatherReport
from .schemas import WeatherResponse
from .weather_service import get_weather
from .alert_service import check_and_alert
from .ai_agent import generate_weather_summary

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Free AI Weather Automation with SendGrid")

# ---------------- ROOT ROUTE ----------------
@app.get("/", tags=["Root"])
def root():
    return {"message": "Weather Automation API is running!"}

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Weather endpoint
@app.get("/weather/{city}", response_model=WeatherResponse, tags=["Weather"])
def weather(city: str, db: Session = Depends(get_db)):
    data = get_weather(city)
    summary = generate_weather_summary(city, data["temperature"], data["description"])
    check_and_alert(city, data["temperature"], data["description"])

    report = WeatherReport(
        city=city,
        temperature=data["temperature"],
        description=data["description"],
        ai_summary=summary
    )

    db.add(report)
    db.commit()
    db.refresh(report)  # <- important to refresh object
    return report
