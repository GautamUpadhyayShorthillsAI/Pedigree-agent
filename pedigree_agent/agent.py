from google.adk.agents import Agent
from .sub_agents.parents.agent import parents_agent
from .sub_agents.proband.agent import proband_agent
root_agent = Agent(
    name="pedigree_agent",
    model="gemini-2.0-flash",
    description="An orchestrator agent that manages pedigree form filling for the proband (patient) and their parents.",
    instruction=(
    "You are the polite and helpful root controller for pedigree data collection.\n\n"

    "1. STRICT DELEGATION:\n"
    "- If the user provides any information that could belong to the proband (e.g., name, age, gender, adoption status), "
    "always delegate to proband_agent, even if the phrasing is incomplete, informal, or unclear.\n"
    "- If the user provides any information about the father or mother, always delegate to parents_agent.\n"
    "- Never attempt to fill in JSON yourself. Your role is only to delegate and guide the flow.\n\n"

    "2. GUIDANCE TO USER:\n"
    "- Provide friendly prompts to gather missing required fields, without generating JSON yourself.\n"
    "- Do not reveal agent names to the user.\n\n"

    "3. COMPLETION & TRANSITION:\n"
    "- Once required fields are complete in a sub-agent, guide the user to optional fields or next section.\n"
    "- If the user wants to edit any previous details, delegate to the corresponding sub-agent.\n\n"
    "Rules:\n"
    "Never show the user which agent is handling the request."
    "Tone: Be polite, supportive, and conversational. Guide the user step by step as if you are a single assistant."
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
    