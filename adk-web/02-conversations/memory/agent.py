import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

from . import instruction

load_dotenv()

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = instruction.INSTRUCTION,
    tools=[google_search],
)
