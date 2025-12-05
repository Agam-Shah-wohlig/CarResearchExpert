from google.adk.agents import LlmAgent
from schema.car_comparison_schema import CarComparisonHTMLOutput
from tools import create_car_comparison_html_output
import os

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

car_merger_agent = LlmAgent(
    name="html_systhesis_agent",
    model=GEMINI_MODEL,
    description="A merger and synthesizer agent that generate HTML and save the file.",
    instruction="""
You are a Merger / Synthesis Agent for automotive research. 

Your task is to generate a car comparison HTML page using the provided template. 
The HTML structure is already available, so you do **not** need to create or modify it. 
You only need to:

1. Take the structured outputs from the two sub-agents:
   - {car1_result} → dictionary with car 1 details
   - {car2_result} → dictionary with car 2 details

2. Fill the template with the data from both cars. The template already contains placeholders for:
   - Model
   - Summary
   - Engine
   - Fuel Type
   - Transmission
   - Max Power
   - Max Torque
   - Mileage
   - Price Range
   - Key Features

3. Save the resulting HTML file using the `file_saver` function. 
   - Filename: `car_comparison.html` (or dynamic names if desired)
   - Folder: `html/`
   - Do the same with style.css as well
4. Do **not** return or output the HTML. Your job is only to generate and save the file.
""",

    tools=[create_car_comparison_html_output],
    output_schema=CarComparisonHTMLOutput,
    output_key="car_comparison_html_output"
)
