from google.adk.agents import Agent
from ...prompts.description import maternal_siblings_description
from ...prompts.prompts_v2 import maternal_siblings_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

maternal_siblings_agent = Agent(
    name="maternal_siblings_agent",
    model="gemini-2.0-flash",
    description=maternal_siblings_description,
    instruction=maternal_siblings_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)

