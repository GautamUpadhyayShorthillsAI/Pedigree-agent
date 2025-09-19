from google.adk.agents import Agent
from ...prompts.description import parents_description
from ...prompts.prompts_v2 import parents_instruction

parents_agent = Agent(
    name="parents_agent",
    model="gemini-2.0-flash",
    description=parents_description,
    instruction=parents_instruction,
)