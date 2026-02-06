from typing import List

from core.models import Field, Soil, Season, Crop
from core.rules import (
    validate_crop_soil,
    validate_crop_season,
    RuleViolation
)


class CropRecommender:
    """
    Recommends valid crops based on
    field, soil, and season constraints.
    """

    def recommend(
        self,
        field: Field,
        soil: Soil,
        season: Season,
        crops: List[Crop]
    ) -> List[Crop]:

        valid_crops = []

        for crop in crops:
            try:
                validate_crop_soil(crop, soil)
                validate_crop_season(crop, season)

                valid_crops.append(crop)

            except RuleViolation:
                continue

        return valid_crops
