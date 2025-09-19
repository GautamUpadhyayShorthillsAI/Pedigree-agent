from google.adk.agents import Agent
from ...prompts.description import proband_description
from ...prompts.prompts_v2 import proband_instruction

proband_agent = Agent(
    name="proband_agent",
    model="gemini-2.0-flash",
    description=proband_description,
    instruction=proband_instruction,
)