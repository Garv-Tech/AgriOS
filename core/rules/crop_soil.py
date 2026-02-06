from core.models import Crop, Soil
from .base import RuleViolation


def validate_crop_soil(crop: Crop, soil: Soil) -> None:
    if soil.soil_type not in crop.soil_compatibility:
        raise RuleViolation(
            f"Crop '{crop.name}' is not compatible with soil '{soil.soil_type}'."
        )
