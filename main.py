import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from pedigree_agent.agent import root_agent
from utils import call_agent_async

load_dotenv()

# ===== PART 1: Initialize Persistent Session Service =====
# Using SQLite database for persistent storage
db_url = "sqlite:///./sessions.db"
session_service = DatabaseSessionService(db_url=db_url)
APP_NAME = "Pedigree Agent"

async def main_async(query:str):
    # Setup constants
    USER_ID = "user_001"

    # ===== PART 3: Session Management - Find or Create =====
    # Check for existing sessions for this user
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )
    print(existing_sessions)
    # If there's an existing session, use it, otherwise create a new one
    if existing_sessions and len(existing_sessions.sessions) > 0:
        # Use the most recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
    else:
        # Create a new session with initial state
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the memory agent
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # ===== PART 5: Interactive Conversation Loop =====
    print("\nWelcome to Pedigree Agent Chat!")
    print("Hello! To get started, are you the proband, or are you filling this form out for someone else? We'll begin with the proband's details.")
    print("Type 'exit' or 'quit' to end the conversation.\n")


    user_input = query

    # Process the user query through the agent
    response = await call_agent_async(runner, USER_ID, SESSION_ID, user_input)
    return response


if __name__ == "__main__":
    asyncio.run(main_async("Hello"))
