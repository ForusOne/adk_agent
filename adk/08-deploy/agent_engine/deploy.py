import os
from dotenv import load_dotenv

import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
from google.adk.agents import Agent

from .agent import root_agent

load_dotenv()

def init_vertexai():

  vertexai.init(
      project=os.getenv("PROJECT_ID"),
      location=os.getenv("LOCATION"),
      staging_bucket=os.getenv("STAGING_BUCKET"),
  )

def test_agent(user_id:str, 
               message:str, ):

  app = AdkApp(agent=root_agent)

  for event in app.stream_query(
      user_id=user_id,
      message=message,
  ):
    outcome = event['content']['parts'][0]['text']
    print(outcome)

def deploy_agent(agent:Agent):

  remote_agent = agent_engines.create(
      agent,
      display_name="currency agent with adk",
      gcs_dir_name = "ai-agent-adk",
      description="This is a simple agent with adk on agent engine.",
      requirements=[
          "google-adk",
          "cloudpickle==3.0",
      ],
      extra_packages = []
  )
  return remote_agent


