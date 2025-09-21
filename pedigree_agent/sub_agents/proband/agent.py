from google.adk.agents import Agent
from ...prompts.description import proband_description
from ...prompts.prompts_v2 import proband_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

proband_agent = Agent(
    name="proband_agent",
    model="gemini-2.5-pro",
    description=proband_description,
    instruction=proband_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)