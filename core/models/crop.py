from .base import CoreModel
from typing import Tuple


class Crop(CoreModel):
    name: str
    growth_duration_days: int
    water_requirement: str
    temperature_range: Tuple[float, float]
    soil_compatibility: list[str]
