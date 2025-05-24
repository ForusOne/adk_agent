
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from tool_callback import agent

async def run_agent(user_query: str):
    """
    Initializes and runs the basic_agent with a sample query.
    """
    print(f"User: {user_query}")

    APP_NAME = "search_assistant"
    USER_ID = "forusone"

    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            )
    
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    
    content = types.Content(role='user', parts=[types.Part(text=user_query)])

    events = runner.run_async(user_id=session.user_id,
                              session_id=session.id,
                              new_message=content,)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text            
            print("Assistant: " + final_response)

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    # parser.add_argument("--country",type=str,help="The name of country",)
    parser.add_argument("--query",type=str,help="The application name of this agent.",)

    args = parser.parse_args()
    asyncio.run(run_agent(user_query=args.query))