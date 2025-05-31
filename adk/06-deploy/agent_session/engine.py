import os
import argparse
from dotenv import load_dotenv

import vertexai
from vertexai import agent_engines

load_dotenv()

def create_agent_engine(agent_name:str,
                        description:str=None):

    # Initialize Vertex AI to deploy Agent Engine. 
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )

    # Create an agent engine instance
    agent_engine = agent_engines.create(
        display_name=agent_name,
        gcs_dir_name=os.getenv("STAGING_BUCKET"),
        description=description,
    )

    return agent_engine

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_session.engine --agent_name forusone """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    
    parser.add_argument("--agent_name",type=str)
    
    args = parser.parse_args()

    agent_engine = create_agent_engine(agent_name=args.agent_name)
    print(f"Agent Engine created : {agent_engine}")
    
