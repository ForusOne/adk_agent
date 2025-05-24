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

import os
from dotenv import load_dotenv
import argparse

import vertexai
from vertexai.preview.reasoning_engines import AdkApp
from google.adk.agents import Agent

from .agent import root_agent
from .agent_mgmt import deploy_agent
from .agent_mgmt import get_agent_engine
from .agent_mgmt import show_agents
from .agent_mgmt import delete_agent

load_dotenv()

def build_adk_app(root_agent:Agent,
              user_id:str,
              query:str,):

    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )
    adk_app = AdkApp(agent=root_agent)

    events = adk_app.stream_query(user_id=user_id, message=query)

    print(f"Unit test in AdkApp : {query}")

    for event in events:
        outcome = event['content']['parts'][0]['text']
        print(outcome)

    return adk_app


if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_engine.deploy --query 'What is the Generative AI?' """)
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--query",type=str,help="The application name of this agent.",)

    args = parser.parse_args()
    user_id = "Forusone"
    query = args.query

    #1. Print all registered agents.
    show_agents()

    #2. Build a adk_app.
    adk_app = build_adk_app(root_agent, user_id, query)

    #3. Deploy the adk_app on Agent Engine.
    display_name = "search agent"
    gcs_dir_name = os.getenv("STAGING_BUCKET")
    description = "AI information search assistant to user's question"
    requirements = [
        "google-adk[vertexai]",
        "google-cloud-aiplatform[adk,agent-engines]",
        "cloudpickle==3.0",
        "python-dotenv",
    ]
    extra_packages = []

    remote_agent = deploy_agent(agent = adk_app, 
                                display_name = display_name, 
                                gcs_dir_name = gcs_dir_name,
                                description = description,
                                requirements = requirements,
                                extra_packages = extra_packages)

    #4. Get the remote agent engine instance.
    remote_agent_engine = get_agent_engine(resource_name = remote_agent.resource_name)

    #5. Execute the query.
    print(f"Outcome from Agent Engine in remote. ")            

    for event in remote_agent_engine.stream_query(
        user_id=user_id,
        message=args.query,):

        outcome = event['content']['parts'][0]['text']
        print(outcome)            


# if __name__ == "__main__":
        
#         resource_name = "projects/721521243942/locations/us-central1/reasoningEngines/1950665569069957120"
#         remote_agent_engine = get_agent_engine(resource_name = resource_name)
#         print(remote_agent_engine)

#         for event in remote_agent_engine.stream_query(
#             user_id="Forusone",
#             message="What is the Generative AI?",):
            
#             print(event)
#             #outcome = event['content']['parts'][0]['text']






