from google.adk.agents import Agent
from ...prompts.description import spouse_description
from ...prompts.prompts_v2 import spouse_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

spouse_agent = Agent(
    name="spouse_agent",
    model="gemini-2.5-pro",
    description=spouse_description,
    instruction=spouse_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)

