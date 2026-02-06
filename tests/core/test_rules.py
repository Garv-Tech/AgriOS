import pytest
from datetime import date
from uuid import uuid4

from core.models import Crop, Soil, Season, Field
from core.rules import (
    validate_crop_soil,
    validate_crop_season,
    validate_field_crop_assignment,
    RuleViolation
)


def test_crop_soil_valid():
    crop = Crop(
        name="Wheat",
        growth_duration_days=120,
        water_requirement="medium",
        temperature_range=(10, 25),
        soil_compatibility=["loamy", "clay"]
    )

    soil = Soil(
        soil_type="loamy",
        ph_level=6.5,
        organic_content=2.1,
        water_retention=0.6,
        last_tested_date=date.today()
    )

    validate_crop_soil(crop, soil)


def test_crop_soil_invalid():
    crop = Crop(
        name="Rice",
        growth_duration_days=150,
        water_requirement="high",
        temperature_range=(20, 35),
        soil_compatibility=["clay"]
    )

    soil = Soil(
        soil_type="sandy",
        ph_level=7.0,
        organic_content=1.2,
        water_retention=0.3,
        last_tested_date=date.today()
    )

    with pytest.raises(RuleViolation):
        validate_crop_soil(crop, soil)


def test_crop_season_valid():
    crop = Crop(
        name="Mustard",
        growth_duration_days=90,
        water_requirement="low",
        temperature_range=(10, 20),
        soil_compatibility=["loamy"]
    )

    season = Season(
        name="Rabi",
        start_month=10,
        end_month=2,
        climate_pattern="cool"
    )

    validate_crop_season(crop, season)


def test_crop_season_invalid():
    crop = Crop(
        name="Sugarcane",
        growth_duration_days=360,
        water_requirement="high",
        temperature_range=(20, 35),
        soil_compatibility=["loamy"]
    )

    season = Season(
        name="Kharif",
        start_month=6,
        end_month=9,
        climate_pattern="monsoon"
    )

    with pytest.raises(RuleViolation):
        validate_crop_season(crop, season)


def test_field_crop_assignment_violation():
    field = Field(
        farmer_id=uuid4(),
        soil_id=uuid4(),
        area_hectares=1.5,
        geo_zone="north-india",
        irrigation_type="canal"
    )

    crop = Crop(
        name="Wheat",
        growth_duration_days=120,
        water_requirement="medium",
        temperature_range=(10, 25),
        soil_compatibility=["loamy"]
    )

    season = Season(
        name="Rabi",
        start_month=10,
        end_month=2,
        climate_pattern="cool"
    )

    with pytest.raises(RuleViolation):
        validate_field_crop_assignment(
            field,
            crop,
            season,
            existing_assignment=True
        )
