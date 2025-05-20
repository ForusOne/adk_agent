import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import built_in_code_execution

load_dotenv()

INSTRUCTION = """
    당신은 계산기 에이전트입니다.
    수학식이 주어지면 Python 코드를 작성하고 실행하여 결과를 계산합니다.
    응답결과는 Python code 및 실행 결과 최종 수치 모두 일반 텍스트로 반환합니다.
"""

code_execution_agent = Agent(
    name = "code_execution_agent",
    model = os.getenv("MODEL"),
    description = "Python 코드를 실행하여 계산을 수행합니다.",
    instruction = INSTRUCTION,
    tools=[built_in_code_execution],
)

root_agent = code_execution_agent