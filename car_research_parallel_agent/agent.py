from google.adk.agents import ParallelAgent
from car_researcher_1 import car_subagent_1
from car_researcher_2 import car_subagent_2


# Create the ParallelAgent
parallel_car_research_agent = ParallelAgent(
    name="car_research_parallel_agent",
    sub_agents=[car_subagent_1, car_subagent_2],
    description="Orchestrates multiple automotive research sub-agents in parallel to gather information about two cars simultaneously.",
 
)