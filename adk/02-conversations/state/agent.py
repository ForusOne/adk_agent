import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면, 그 질문에 대한 구글 검색(google_search) 툴을 수행하고,그 결과를 바탕으로 답변을 제공해야 합니다.
    답변을 할 때는 아래와 같은 형식을 따라야 합니다.

    1. 질문: [질문 내용]
    2. 출처 정보 : [출처 이름]
    3. 답변: [답변 내용]
    4. 추가 정보: [추가 정보 내용]

"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[google_search],
    output_key="last_answer"
)
