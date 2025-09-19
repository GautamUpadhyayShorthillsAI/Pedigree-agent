from google.adk.agents import Agent
from ...prompts.description import siblings_description
from ...prompts.prompts_v2 import siblings_instruction

siblings_agent = Agent(
    name="siblings_agent",
    model="gemini-2.0-flash",
    description=siblings_description,
    instruction=siblings_instruction,
)   