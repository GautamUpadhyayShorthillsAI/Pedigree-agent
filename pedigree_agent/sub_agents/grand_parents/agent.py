from google.adk.agents import Agent
from ...prompts.description import grand_parents_description
from ...prompts.prompts_v2 import grand_parents_instruction

grand_parents_agent = Agent(
    name="grand_parents",
    model="gemini-2.0-flash",
    description=grand_parents_description,
    instruction=grand_parents_instruction,
)

