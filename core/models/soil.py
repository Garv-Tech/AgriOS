from .base import CoreModel
from datetime import date


class Soil(CoreModel):
    soil_type: str
    ph_level: float
    organic_content: float
    water_retention: float
    last_tested_date: date
