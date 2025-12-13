from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    ai_summary: str

    class Config:
        orm_mode = True
