from google.adk.agents import Agent
from ...prompts.description import parents_description
from ...prompts.prompts_v2 import parents_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

parents_agent = Agent(
    name="parents_agent",
    model="gemini-2.0-flash",
    description=parents_description,
    instruction=parents_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)