from google.adk.agents import Agent
from .sub_agents.parents.agent import parents_agent
from .sub_agents.proband.agent import proband_agent
from .sub_agents.siblings.agent import siblings_agent
root_agent = Agent(
    name="pedigree_agent",
    model="gemini-2.0-flash",
    description="An orchestrator agent that manages pedigree form filling for the proband (patient), their parents, and siblings.",
    instruction=(
    "You are the polite and helpful root controller for pedigree data collection.\n\n"

    "1. STRICT DELEGATION:\n"
    "- If the user provides any information that could belong to the proband (e.g., name, age, gender, adoption status), "
    "always delegate to proband_agent, even if the phrasing is incomplete, informal, or unclear.\n"
    "- If the user provides any information about the father or mother, always delegate to parents_agent.\n"
    "- If the user provides any information about siblings (e.g., brother, sister, sibling names), "
    "always delegate to siblings_agent.\n"
    "- Never attempt to fill in JSON yourself. Your role is only to delegate and guide the flow.\n\n"

    "2. GUIDANCE TO USER:\n"
    "- Provide friendly prompts to gather missing required fields, without generating JSON yourself.\n"
    "- Do not reveal agent names to the user.\n\n"

    "3. COMPLETION & TRANSITION:\n"
    "- Once required fields are complete in a sub-agent, guide the user to optional fields or next section.\n"
    "- Suggested flow: Proband → Parents → Siblings (but be flexible based on user input).\n"
    "- If the user wants to edit any previous details, delegate to the corresponding sub-agent.\n"
    "- BATCH OPERATIONS: Support updating multiple family members simultaneously. When user mentions multiple people (e.g., '3 siblings, father, grandmother'), collect all changes in sequence but process them as a batch.\n"
    "- LISTING: When user requests to see all family members, compile and display information from all sub-agents.\n"
    "- LASTNAME INHERITANCE ORCHESTRATION: Coordinate bidirectional lastname updates across all family members:\n"
    "  * Monitor context.state['pending_lastname_updates'] for cross-agent updates\n"
    "  * When one agent suggests updating another family member's lastname, coordinate the update\n"
    "  * Prevent circular updates by tracking update sources\n"
    "  * Always ask user confirmation before cascading updates\n\n"
    "Rules:\n"
    "Never show the user which agent is handling the request."
    "Tone: Be polite, supportive, and conversational. Guide the user step by step as if you are a single assistant."
    ),
    sub_agents=[parents_agent, proband_agent, siblings_agent],
)



# Complete JSON structure for pedigree data collection:

# Final combined JSON format:
# {
#   "proband": {
#     "firstName": "string", // required
#     "lastName": "string", 
#     "gender": "string", // Values: "male", "female", "other" // required
#     "age": "string", // required
#     "dob": "string", // Date of birth
#     "isAlive": "boolean",
#     "isAdopted": "string", // Values: "AdoptedIn", "AdoptedOut", or null
#   },
#   "parents": {
#     "father": {
#       "firstName": "string", // required
#       "lastName": "string",
#       "sex": "string", // "M" for male
#       "age": "string",
#       "dob": "string",
#       "isAlive": "boolean",
#       "additionalInfo": "string"
#     },
#     "mother": {
#       "firstName": "string", // required
#       "lastName": "string",
#       "sex": "string", // "F" for female
#       "age": "string",
#       "dob": "string", 
#       "isAlive": "boolean",
#       "additionalInfo": "string"
#     }
#   },
#   "siblings": [
#     {
#       "firstName": "string", // required
#       "lastName": "string",
#       "relationship": "string", // Values: "brother", "sister" // required
#       "age": "string",
#       "dob": "string", // Date of birth in dd/mm/yyyy format
#       "isAlive": "string", // Values: "alive", "deceased", "unknown"
#       "adoptionStatus": "string", // Values: "adopted_in", "adopted_out", "unknown", null
#       "siblingType": "string", // Values: "full", "half" // required
#       "commonParent": "string", // Values: "father", "mother" // required for half-siblings, null for full
#       "otherParentName": "string" // Name of non-shared parent for half-siblings, null for full
#     }
#   ]
# }