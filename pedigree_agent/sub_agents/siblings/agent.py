from google.adk.agents import Agent
from ...prompts.description import siblings_description
from ...prompts.prompts_v2 import siblings_instruction
from ...tools.age_calculator import age_calculator_tool
from ...tools.gender_guesser import gender_guesser_tool

siblings_agent = Agent(
    name="siblings_agent",
    model="gemini-2.5-pro",
    description=siblings_description,
    instruction=siblings_instruction,
    tools=[age_calculator_tool, gender_guesser_tool],
)   