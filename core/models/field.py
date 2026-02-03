from .base import CoreModel
from uuid import UUID


class Field(CoreModel):
    farmer_id: UUID
    soil_id: UUID
    area_hectares: float
    geo_zone: str
    irrigation_type: str
