from datetime import date
from uuid import uuid4

from core.models import Field, Soil, Season, Crop
from services.advisory.recommender import CropRecommender


def test_crop_recommendation_basic():
    # Field
    field = Field(
        farmer_id=uuid4(),
        soil_id=uuid4(),
        area_hectares=2.0,
        geo_zone="north-india",
        irrigation_type="canal"
    )

    # Soil
    soil = Soil(
        soil_type="loamy",
        ph_level=6.8,
        organic_content=2.5,
        water_retention=0.7,
        last_tested_date=date.today()
    )

    # Season
    season = Season(
        name="Rabi",
        start_month=10,
        end_month=2,
        climate_pattern="cool"
    )

    # Crops
    wheat = Crop(
        name="Wheat",
        growth_duration_days=120,
        water_requirement="medium",
        temperature_range=(10, 25),
        soil_compatibility=["loamy"]
    )

    rice = Crop(
        name="Rice",
        growth_duration_days=150,
        water_requirement="high",
        temperature_range=(20, 35),
        soil_compatibility=["clay"]
    )

    mustard = Crop(
        name="Mustard",
        growth_duration_days=90,
        water_requirement="low",
        temperature_range=(10, 20),
        soil_compatibility=["loamy"]
    )

    crops = [wheat, rice, mustard]

    recommender = CropRecommender()

    result = recommender.recommend(field, soil, season, crops)

    names = [c.name for c in result]

    # Wheat and Mustard fit
    assert "Wheat" in names
    assert "Mustard" in names

    # Rice should be rejected
    assert "Rice" not in names
