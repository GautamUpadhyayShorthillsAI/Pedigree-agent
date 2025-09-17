from google.adk.agents import Agent

parents_agent = Agent(
    name="parents_agent",
    model="gemini-2.0-flash",
    description="Collects and structures the father and mother information required for the pedigree form.",
    instruction=(
        "You are responsible for filling the parents JSON. "
        "The structure is:\n"
        "{\n"
        '  "father": {\n'
        '    "firstName": "string", (required)\n'
        '    "lastName": "string",\n'
        '    "sex": "M",\n'
        '    "age": "string",\n'
        '    "dob": "string",\n'
        '    "isAlive": boolean,\n'
        '    "additionalInfo": "string"\n'
        '  },\n'
        '  "mother": {\n'
        '    "firstName": "string", (required)\n'
        '    "lastName": "string",\n'
        '    "sex": "F",\n'
        '    "age": "string",\n'
        '    "dob": "string",\n'
        '    "isAlive": boolean,\n'
        '    "additionalInfo": "string"\n'
        '  }\n'
        "}\n\n"
        "Rules:\n"
        "- Always return the JSON in the exact structure.\n"
        "- If required fields (firstName) are missing for father or mother, return the partially filled JSON and explicitly ask the user for the missing fields.\n"
        "- Do not invent values. Only use what the user provides.\n"
        "- Ensure that father's sex is 'M' and mother's sex is 'F'.\n"
    ),
)