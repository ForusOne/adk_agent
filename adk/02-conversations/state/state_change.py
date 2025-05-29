import time
import asyncio
import argparse
from dotenv import load_dotenv

from google.adk.events import Event, EventActions
from google.adk.sessions import InMemorySessionService

from state import agent

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str,):

    session_service = InMemorySessionService()

    session = session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
        state={"user:login_count": 0, "task_status": "idle"}
    )
    
    print(f"Initial state: {session.state}")

    # --- Define State Changes ---
    current_time = time.time()
    state_changes = {
        "task_status": "active",              # Update session state
        "user:login_count": session.state.get("user:login_count", 0) + 1, # Update user state
        "user:last_login_ts": current_time,   # Add user state
        "temp:validation_needed": True        # Add temporary state (will be discarded)
    }

    # --- Create Event with Actions ---
    actions_with_update = EventActions(state_delta=state_changes)
    system_event = Event(
        invocation_id="inv_login_update",
        author="system", # Or 'agent', 'tool' etc.
        actions=actions_with_update,
        timestamp=current_time
    )

    # --- Append the Event (This updates the state) ---
    session_service.append_event(session, system_event)
    print("`append_event` called with explicit state delta.")

    # --- Check Updated State ---
    updated_session = session_service.get_session(app_name=app_name,
                                                user_id=user_id, 
                                                session_id=session_id)
    print(f"State after event: {updated_session.state}")

if __name__ == "__main__":

    load_dotenv()

    print("Running the agent...")
    print("Usage : python main.py --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()

    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id, 
                          session_id = args.session_id,))
    