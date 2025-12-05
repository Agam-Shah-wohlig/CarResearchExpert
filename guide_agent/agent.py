from google.adk.agents import LlmAgent
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

car_guide_agent = LlmAgent(
    name="guide_agent",
    model=GEMINI_MODEL,
    description="An Agent that guides the next Parallel Agent.",
    instruction="""
You are a guide agent for car comparisons.

1. Receive the user query about comparing two cars, for example: "Compare Audi A3 vs BMW i3".
2. Extract exactly two car names from the query.
3. If the car names are unclear, incomplete, or lack specific variants, ask the user for clarification until both car names are precise.
4. Once the correct car names are confirmed, output them using the output key "cars_name" in the following structure:

   cars_name = {
       "car_1": "<First Car Name>",
       "car_2": "<Second Car Name>"
   }

5. Do not perform any searches, analysis, or comparisons. Your only responsibility is to extract and return the correct two car names in the required structured format.
6. If the cars name are not provide do not call the next agent in queue.
""",
    output_key="cars_name"
) 