from dotenv import load_dotenv
import os

from google.genai import types
from google.adk.sessions import Session, BaseSessionService, InMemorySessionService
from google.adk.sessions import VertexAiSessionService

from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner, RunConfig, StreamingMode

from session import agent

load_dotenv()

PROJECT_ID = os.environ['PROJECT_ID']
LOCATION = os.environ['LOCATION']

# Example using a local SQLite file:

REASONING_ENGINE_APP_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/1769993818393804800"
session_service = VertexAiSessionService(project=PROJECT_ID, location=LOCATION)

initial_state = {"initial_key": "initial_value"}

#------------------------------------------------------------

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str):
    """
    Initializes and runs the agent with a sample query.
    Parameters:
        app_name (str): The name of the application.
        user_id (str): The ID of the user.
        session_id (str): The ID of the session.
        session_service (BaseSessionService): The session service.
    Returns None.
    
    """
    app_name = REASONING_ENGINE_APP_NAME

    existing_sessions = session_service.list_sessions(
        app_name=app_name,
        user_id=user_id,
    )

    if existing_sessions and len(existing_sessions.sessions) > 0:
        # Use the most recent session
        session_id = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {session_id}")
    else:
        # Create a new session with initial state
        new_session = session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            state=initial_state,
        )
        session_id = new_session.id
        print(f"Created new session: {session_id}")

    
    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)
    
    run_config = RunConfig(
        response_modalities = ["TEXT"],
        streaming_mode= StreamingMode.SSE,
        max_llm_calls = 10
    )

    while True:

        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        content = types.Content(role='user', parts=[types.Part(text=user_input)])

        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content,
                                run_config=run_config)

        async for event in events:
            await asyncio.create_task(print_session(app_name = app_name,
                                                    user_id = user_id,
                                                    session_id = session_id,
                                                    session_service = session_service))

            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("Assistant: " + final_response)

#------------------------------------------------------------

async def print_session(app_name: str,
                        user_id: str,
                        session_id: str,
                        session_service: BaseSessionService):
    """
    Retrieves the session from the session service.
    Parameters:
        app_name (str): The name of the application.
        user_id (str): The ID of the user.
        session_id (str): The ID of the session.
        session_service (BaseSessionService): The session service.
    Returns None.
    """

    session  = session_service.get_session(app_name=app_name,
                                user_id=user_id,
                                session_id=session_id,)
    

    print(f"--- Examining Session Properties ---")
    print(f"ID (`id`):                {session.id}")
    print(f"Application Name (`app_name`): {session.app_name}")
    print(f"User ID (`user_id`):         {session.user_id}")
    print(f"State (`state`):           {session.state}") # Note: Only shows initial state here
    print(f"Events (`events`):         {session.events}") # Initially empty
    print(f"Last Update (`last_update_time`): {session.last_update_time:.2f}")
    print(f"---------------------------------")

#------------------------------------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()


    asyncio.run(run_agent(app_name = args.app_name, 
                                user_id = args.user_id, 
                                session_id = args.session_id,))
    