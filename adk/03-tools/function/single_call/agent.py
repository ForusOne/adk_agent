import os
from dotenv import load_dotenv
from google.adk.agents import Agent

from . import function

load_dotenv()

INSTRUCTION = """ 당신은 환율 정보를 검색해서 답해주는 AI Agent 입니다.
    기준 환율과 변환대상 환율을 알려주면 해당 제시된 날짜기준의 환율정보를 알려주세요.
    답변 형식은 아래와 같습니다.
    - 기준환율: USD
    - 변환대상환율: KRW
    - 날짜 : 2025-05-20
    - 환율 : 

"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[function.get_exchange_rate],

)
