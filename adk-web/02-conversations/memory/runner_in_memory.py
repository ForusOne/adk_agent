from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner, RunConfig, StreamingMode

from memory import agent

async def run_basic_agent(user_query: str):
    """
    Initializes and runs the basic_agent with a sample query.
    """
    print(f"User: {user_query}")

    APP_NAME = "Search_Assistant"
    USER_ID = "forusone"

    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            state={"initial_key": "initial_value"})
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    
    content = types.Content(role='user', parts=[types.Part(text=user_query)])

    # https://google.github.io/adk-docs/runtime/runconfig/#runtime-parameters    
    run_config = RunConfig(
        response_modalities = ["TEXT"],
        streaming_mode= StreamingMode.SSE,
        max_llm_calls = 10
    )

    events = runner.run_async(user_id=session.user_id,
                              session_id=session.id,
                              new_message=content,
                              run_config=run_config)

    async for event in events:

        if event.is_final_response():
            final_response = event.content.parts[0].text            
            print("Assistant: " + final_response)

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument(
        "--query",
        type=str,
        help="The query/message to send to the agent.",
    )
    args = parser.parse_args()
    asyncio.run(run_basic_agent(user_query=args.query))