from sqlalchemy import Column, Integer, String, Float
from .db import Base

class WeatherReport(Base):
    __tablename__ = "weather_reports"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)
    ai_summary = Column(String)
