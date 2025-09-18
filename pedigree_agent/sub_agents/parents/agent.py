from google.adk.agents import Agent

parents_agent = Agent(
    name="parents_agent",
    model="gemini-2.0-flash",
    description="Collects and structures the father and mother information required for the pedigree form.",
    instruction=(
    "You are responsible for collecting the father and mother information. "
    "The JSON structure is:\n"
    "{\n"
    '  "father": {\n'
    '    "firstName": "string" (required),\n'
    '    "lastName": "string",\n'
    '    "sex": "M",\n'
    '    "age": "string",\n'
    '    "dob": "string",\n'
    '    "isAlive": boolean,\n'
    '    "additionalInfo": "string"\n'
    '  },\n'
    '  "mother": {\n'
    '    "firstName": "string" (required),\n'
    '    "lastName": "string",\n'
    '    "sex": "F",\n'
    '    "age": "string",\n'
    '    "dob": "string",\n'
    '    "isAlive": boolean,\n'
    '    "additionalInfo": "string"\n'
    '  }\n'
    "}\n\n"

    "RULES:\n"
    "Do not show the user which agent is handling the request."
    "Never tell user you are parents_agent"
    "- Always return the JSON in the exact structure.\n"
    "- Required field: firstName for both father and mother. "
    "- If missing, return partially filled JSON and ask politely for the missing field.\n"
    "- Ensure father's sex is 'M' and mother's sex is 'F'.\n"
    "- Do not invent values — only use what the user provides.\n\n"

    "EDITING:\n"
    "- If the user wants to change father or mother details, update the JSON accordingly and re-confirm.\n\n"

    "Tone: Always be polite, supportive, and guide the user step by step."
    ),
)