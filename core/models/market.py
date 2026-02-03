from .base import CoreModel
from uuid import UUID


class Market(CoreModel):
    crop_id: UUID
    region: str
    price_per_unit: float
    demand_level: str
