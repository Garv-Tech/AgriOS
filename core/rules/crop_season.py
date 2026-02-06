from core.models import Crop, Season
from .base import RuleViolation


def validate_crop_season(crop: Crop, season: Season) -> None:
    """
    Validates whether a crop can complete its growth
    within the given season duration.
    """

    # Handle seasons that cross year boundary (e.g., Oct -> Feb)
    if season.end_month >= season.start_month:
        months = season.end_month - season.start_month + 1
    else:
        months = (12 - season.start_month + 1) + season.end_month

    season_length_days = months * 30

    if crop.growth_duration_days > season_length_days:
        raise RuleViolation(
            f"Crop '{crop.name}' cannot fit in season '{season.name}'."
        )
