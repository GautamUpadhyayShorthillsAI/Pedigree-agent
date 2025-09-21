from google.adk.agents import Agent
from ...prompts.description import grand_parents_description
from ...prompts.prompts_v2 import grand_parents_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

grand_parents_agent = Agent(
    name="grand_parents",
    model="gemini-2.5-pro",
    description=grand_parents_description,
    instruction=grand_parents_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)

