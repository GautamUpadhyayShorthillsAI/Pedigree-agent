from google.adk.agents import Agent
from ...prompts.description import paternal_siblings_description
from ...prompts.prompts_v2 import paternal_siblings_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

paternal_siblings_agent = Agent(
    name="paternal_siblings_agent",
    model="gemini-2.5-pro",
    description=paternal_siblings_description,
    instruction=paternal_siblings_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)

