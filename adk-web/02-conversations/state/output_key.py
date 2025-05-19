import asyncio
import time
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from state import agent

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str,):
    """
    Initializes and runs the agent with a sample query.
    Parameters:
        app_name (str): The name of the application.
        user_id (str): The ID of the user.
        session_id (str): The ID of the session.
    Returns None.
    
    """

    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=app_name, 
                                            user_id=user_id, 
                                            session_id=session_id)

    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)
    
    print(f"Initial state: {session.state}")

    while True:

        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        content = types.Content(role='user', parts=[types.Part(text=user_input)])

        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("Assistant: " + final_response)

        updated_session = session_service.get_session(app_name = app_name, 
                                                     user_id = user_id, 
                                                     session_id = session_id)

        print(f"State after agent run: {updated_session.state}")

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
    