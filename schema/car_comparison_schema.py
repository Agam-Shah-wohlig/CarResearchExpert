# schema/car_comparison_schema.py
from pydantic import BaseModel, Field

class CarComparisonHTMLOutput(BaseModel):
    saved_file_path: str = Field(..., description="Path where the HTML file was saved")
