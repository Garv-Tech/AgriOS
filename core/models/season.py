from .base import CoreModel


class Season(CoreModel):
    name: str  # Kharif / Rabi / Zaid
    start_month: int
    end_month: int
    climate_pattern: str
