import os
from dotenv import load_dotenv
import asyncio
import argparse

from google.adk.sessions import InMemorySessionService

from google.adk.memory import VertexAiRagMemoryService
from google.adk.memory import InMemoryMemoryService 

from memory import runner


if __name__ == "__main__":

    load_dotenv()

    print("Running the agent...")
    print("Usage : python main.py --type <memory_type> --app_name <app_name> --user_id <user_id> --session_id <session_id>")
    print("Usage : session type : in_memory, rag_corpus")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--type",type=str,help="The type of session",)
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()
    
    session_service = InMemorySessionService()

    if args.type == "in_memory":
        memory_service = InMemoryMemoryService()
    
    elif args.type == "rag_corpus":

        PROJECT_ID = os.environ['PROJECT_ID']
        LOCATION = os.environ['LOCATION']
        CORPUS_ID = os.environ['CORPUS_ID']

        RAG_CORPUS_RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{CORPUS_ID}"

        memory_service = VertexAiRagMemoryService(
            rag_corpus=RAG_CORPUS_RESOURCE_NAME,
            similarity_top_k=10,
            vector_distance_threshold=0.2
        )
    
    else:
        raise ValueError("Invalid session type. Choose 'in_memory' or 'rag_corpus'.")

    asyncio.run(runner.run_agent(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 session_id = args.session_id,
                                 ))
    