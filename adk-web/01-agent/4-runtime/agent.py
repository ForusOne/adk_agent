import os
from dotenv import load_dotenv
from google.adk.agents import Agent
load_dotenv()

INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면, 그 질문에 대한 답변을 제공해야 합니다.
    답을 제공할 때는 최대한 간결하고 명확하게 작성해야 합니다.
"""

root_agent = Agent(
    name = "runtime_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
)

