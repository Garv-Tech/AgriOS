from .base import CoreModel


class Farmer(CoreModel):
    name: str
    region: str
    experience_years: int
    preferred_language: str
    farm_type: str  # small / medium / large
