from core.models import Field, Crop, Season
from .base import RuleViolation


def validate_field_crop_assignment(
    field: Field,
    crop: Crop,
    season: Season,
    existing_assignment: bool
) -> None:
    if existing_assignment:
        raise RuleViolation(
            f"Field {field.id} already has a crop in '{season.name}'."
        )
