# Copyright 2025 Forusone(forusone777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from event import agent

async def run_agent():

    """
    Asynchronously runs the AI agent with the provided user query.

    This function creates a user session, initializes the agent runner, and sends the user's query
    to the agent. It streams the agent's responses, prints event details for each step, and displays
    the final response from the agent in the console.

    Args:
        None
    Returns:
        None
    """

    APP_NAME = "AI_assistant"
    USER_ID = "Forusone"

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            state={"initial_key": "initial_value"})
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    

    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit","quit"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=query)])

        events = runner.run_async(user_id=session.user_id,
                                session_id=session.id,
                                new_message=content,
                                )

        async for event in events:
            print("\n\n-------------------------")
            print(f"event : {event}")
            print("-------------------------\n\n")

            print(f"event.invocation_id: {event.invocation_id}")
            print(f"event.author: {event.author}")
            print(f"event.actions: {event.actions}")
            print(f"event.long_running_tool_ids: {event.long_running_tool_ids}")
            print(f"event.branch: {event.branch}")    
            print(f"event.id: {event.id}")
            print(f"event.get_function_calls(): {event.get_function_calls()}")        
            print(f"event.get_function_responses(): {event.get_function_responses()}")        
            print(f"event.has_trailing_code_execution_result(): {event.has_trailing_code_execution_result()}")        
            print(f"event.is_final_response(): {event.is_final_response()}")        
            
            if event.grounding_metadata is not None:
                print("\n\n-----------< Grounding service information >--------------")
                for grounding_chunk in event.grounding_metadata.grounding_chunks:
                    print(f"\n\n--------[ Title: {grounding_chunk.web.title} ]----------")
                    print(f"* grounding_chunk.web.domain: {grounding_chunk.web.domain}")
                    print(f"* grounding_chunk.web.url: {grounding_chunk.web.uri}")
                
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print(f"\n 🤖 AI Assistant: {final_response}\n")

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    args = parser.parse_args()
    asyncio.run(run_agent())