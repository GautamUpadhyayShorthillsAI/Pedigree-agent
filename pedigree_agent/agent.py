from google.adk.agents import Agent
from .sub_agents.parents.agent import parents_agent
from .sub_agents.proband.agent import proband_agent
from .sub_agents.siblings.agent import siblings_agent
from .sub_agents.grand_parents.agent import grand_parents_agent
from .prompts.prompts_v2 import root_instruction
from .prompts.description import root_description

root_agent = Agent(
    name="pedigree_agent",
    model="gemini-2.0-flash",
    description=root_description,
    instruction=root_instruction,
    sub_agents=[parents_agent, proband_agent, siblings_agent, grand_parents_agent],
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

# grand_parents
# {
#   "grandfather": {
#     "firstName": "string",
#     "lastName": "string",
#     "sex": "string", // "M"
#     "age": "string", 
#     "isAlive": "boolean",
#     "additionalInfo": "string"
#   },
#   "grandmother": {
#     "firstName": "string",
#     "lastName": "string", 
#     "sex": "string", // "F"
#     "age": "string",
#     "isAlive": "boolean", 
#     "additionalInfo": "string"
#   }
# }

# grand_parents
# {
#     "Paternal Grand Parents":{
#         "grandfather": {
#             "firstName": "string", /required
#             "lastName": "string",
#             "sex": "string", // "M"
#             "age": "string", 
#             "isAlive": "boolean",
#             "additionalInfo": "string"
#         },
#         "grandmother": {
#             "firstName": "string", / required
#             "lastName": "string", 
#             "sex": "string", // "F"
#             "age": "string",
#             "isAlive": "boolean", 
#             "additionalInfo": "string"
#         }
#     },
#     "Maternal Grand Parents":{
#         "grandfather": {
#             "firstName": "string", / requires
#             "lastName": "string",
#             "sex": "string", // "M"
#             "age": "string", 
#             "isAlive": "boolean",
#             "additionalInfo": "string"
#         },
#         "grandmother": {
#             "firstName": "string", /required
#             "lastName": "string", 
#             "sex": "string", // "F"
#             "age": "string",
#             "isAlive": "boolean", 
#             "additionalInfo": "string"
#         }
#     }
# }


