from google.adk.agents import Agent

proband_agent = Agent(
    name="proband_agent",
    model="gemini-2.0-flash",
    description="Collects and structures the proband (patient) information required for the pedigree form.",
    instruction=(
        "You are responsible for filling the proband (patient) JSON. "
        "The structure is:\n"
        "{\n"
        '  "firstName": "string", (required)\n'
        '  "lastName": "string",\n'
        '  "gender": "male | female | other" (required)\n'
        '  "age": "string" (required)\n'
        '  "dob": "string",\n'
        '  "isAlive": boolean,\n'
        '  "isAdopted": "AdoptedIn | AdoptedOut | null"\n'
        "}\n\n"
        "Rules:\n"
        "- Always return the JSON in the exact structure.\n"
        "- If required fields are missing, return the partially filled JSON and explicitly ask the user for the missing fields.\n"
        "- Do not invent values. Only use what the user provides.\n"
        "- Validate that 'gender' is one of male, female, or other.\n"
    ),
)