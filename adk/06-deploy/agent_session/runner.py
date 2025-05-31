
import os 
import argparse
import asyncio
from dotenv import load_dotenv

from google.genai import types
from google.adk.sessions import VertexAiSessionService
from google.adk.runners import Runner

from agent_session import agent

load_dotenv()

#-----------------------------[call_agent]-----------------------------

def call_agent(runner, 
               user_id:str,
               session_id:str,
               query:str):

    content = types.Content(role='user', parts=[types.Part(text=query)])
    
    events = runner.run(
        user_id=user_id, session_id=session_id, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print(f"\n 🤖 AI Assistant: {final_response}\n")

#-----------------------------[run_agent]-----------------------------

def run_agent(agent_engine_id:str,
                    user_id:str,
                    query:str,
                    session_id:str = None,):
    
    # Create the ADK runner with VertexAiSessionService
    session_service = VertexAiSessionService(os.getenv("PROJECT_ID"), os.getenv("LOCATION"))

    runner = Runner(
        agent=agent.root_agent,
        app_name=agent_engine_id,
        session_service=session_service)

    # Create a session
    session = session_service.create_session(
        app_name=agent_engine_id,
        user_id=user_id,
        session_id=session_id)

    while True:
        query = input("\n 👤 User: ")
        if query.lower() == "exit":
            break

        call_agent(runner, 
                   user_id = user_id, 
                   session_id = session.id, 
                   query = query)

# #-----------------------------[update_remote_agent]-----------------------------

# def update_remote_agent(resource_name:str):

#     # Initialize Vertex AI to deploy Agent Engine. 
#     vertexai.init(
#         project=os.getenv("PROJECT_ID"),
#         location=os.getenv("LOCATION"),
#         staging_bucket=os.getenv("STAGING_BUCKET"),
#     )

#     requirements = [
#         "google-adk[vertexai]",
#         "google-cloud-aiplatform[adk,agent-engines]",
#         "cloudpickle==3.0",
#         "python-dotenv",
#     ]
#     print(f"\n Resource Name : {resource_name}\n")
#     remote_agent_engine = get_agent_engine(resource_name = resource_name)
#     # print(f"\n Reource name : {remote_agent_engine.display_name}\n")
#     print(f"\n Remote Agent Engine : {remote_agent_engine}\n")
    
#     agent_engines.update(resource_name=remote_agent_engine.name, 
#                          gcs_dir_name = os.getenv("STAGING_BUCKET"),
#                          description = "AI information search assistant to user's question",                        
#                          agent_engine=remote_agent_engine, 
#                          requirements=requirements)


#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_session.runner --agent_engine_id 112774708637728768 --user_id forus --session_id 8517270617299353600 """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    
    parser.add_argument("--agent_engine_id",type=str)
    parser.add_argument("--user_id",type=str)
    parser.add_argument("--session_id",type=str)
    parser.add_argument("--query",type=str)
    
    args = parser.parse_args()

    agent_engine_id = args.agent_engine_id
    query = args.query
    user_id = args.user_id
    session_id = args.session_id

    run_agent(agent_engine_id=args.agent_engine_id,
                          user_id=args.user_id,
                          session_id=args.session_id,
                          query=args.query)
    
    deploy_agent