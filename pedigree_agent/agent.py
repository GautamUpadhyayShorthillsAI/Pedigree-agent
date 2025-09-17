from google.adk.agents import Agent
from .sub_agents.parents.agent import parents_agent
from .sub_agents.proband.agent import proband_agent


root_agent = Agent(
    name="pedigree_agent",
    model="gemini-2.0-flash",
    description="An orchestrator agent that manages pedigree form filling for the proband (patient) and their parents.",
    instruction=(
        "You are the root controller for pedigree data collection. "
        "Your job is to understand the user's intent and delegate tasks to the correct sub-agent: "
        "- If the user provides or asks about the proband/patient, call the proband_agent. "
        "- If the user provides or asks about the father or mother, call the parents_agent. "
        "Always return the structured JSON output from the corresponding sub-agent. "
        "Do not modify the JSON yourself — only orchestrate the conversation and route correctly."
    ),
    sub_agents=[parents_agent, proband_agent],
)



# need to get the json for the patient and parents
# patient:
    # {
    #   "firstName": "string", :required
    #   "lastName": "string", 
    #   "gender": "string", // Values: "male", "female", "other" :required
    #   "age": "string", :required
    #   "dob": "string", // Date of birth
    #   "isAlive": "boolean",
    #   "isAdopted": "string", // Values: "AdoptedIn", "AdoptedOut", or null
    # }

# parents:

    # {
    #   "father": {
    #     "firstName": "string", :required
    #     "lastName": "string",
    #     "sex": "string", // "M" for male
    #     "age": "string",
    #     "dob": "string",
    #     "isAlive": "boolean",
    #     "additionalInfo": "string"
    #   },
    #   "mother": {
    #     "firstName": "string", :required
    #     "lastName": "string",
    #     "sex": "string", // "F" for female
    #     "age": "string",
    #     "dob": "string", 
    #     "isAlive": "boolean",
    #     "additionalInfo": "string"
    #   }
    # }