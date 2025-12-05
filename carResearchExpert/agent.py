from google.adk.agents import SequentialAgent
from car_research_parallel_agent.agent import parallel_car_research_agent
from html_systhesis_agent import car_merger_agent
from guide_agent import car_guide_agent

# --- SequentialAgent (Orchestrates the workflow) ---
sequential_pipeline_agent = SequentialAgent(
    name="carResearchExpert",
    sub_agents=[car_guide_agent,parallel_car_research_agent, car_merger_agent],
    description="Runs parallel car research agents and then merges their results into a comparison HTML page."
)

# Root agent for execution
root_agent = sequential_pipeline_agent
