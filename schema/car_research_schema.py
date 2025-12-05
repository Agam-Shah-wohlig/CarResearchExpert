from pydantic import BaseModel, Field
from typing import List, Optional

class VariantInfo(BaseModel):
    name: str = Field(..., description="Name of the car variant/trim.")
    engine: Optional[str] = Field(None, description="Engine type/specification.")
    power: Optional[str] = Field(None, description="Horsepower or power output.")
    torque: Optional[str] = Field(None, description="Torque rating, if available.")
    transmission: Optional[str] = Field(None, description="Transmission type.")
    drivetrain: Optional[str] = Field(None, description="FWD/RWD/AWD, etc.")
    fuel_type: Optional[str] = Field(None, description="Petrol/Diesel/EV/Hybrid/etc.")
    mileage_or_range: Optional[str] = Field(None, description="Mileage (ICE) or range (EV).")
    key_features: Optional[List[str]] = Field(None, description="Notable features of the variant.")
    price_range: Optional[str] = Field(None, description="Price or estimated price range.")

class CarResearchOutput(BaseModel):
    car_model: str = Field(..., description="The main car model researched.")
    summary: str = Field(..., description="A 2–4 sentence concise overview of the findings.")
    top_variants: List[VariantInfo] = Field(..., description="Detailed list of top variants and their specifications.")
    sources: Optional[List[str]] = Field(None, description="List of URLs or source names referenced from the search.")

