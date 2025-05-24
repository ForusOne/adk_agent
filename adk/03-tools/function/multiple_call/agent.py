import os
from dotenv import load_dotenv
from google.adk.agents import Agent

from . import function

load_dotenv()

INSTRUCTION = """ 당신은 환율 정보와 주식정보를 검색해서 답해주는 AI Agent 입니다.
    
    1. 환율정보 검색
        기준 환율과 변환대상 환율을 알려주면 해당 제시된 날짜기준의 환율정보를 알려주세요.
        주어진 질문에서 대상 환율 및 변환대상환율 그리고 날짜 정보를 찾아서 'get_exchange_rate' 툴에게 전달해서 조회해주세요.
        답변 형식은 아래와 같습니다.
        - 기준 환율: USD
        - 변환대상환율: KRW
        - 날짜 : 2025-05-20
        - 환율정보: 1400
    
    2. 주식정보 검색
        주식 정보는 주어진 symbol기준으로 오늘 기준 날짜의 주식가격을 알려주세요.
        주어진 회사 이름에 대해서 symbol을 찾아서 'get_stock_price' 툴에게 전달해서 조회해주세요.
        답변 형식은 아래와 같습니다.
        - 주식정보 : Google
        - 날짜 : 2025-05-20
        - 주식가격 : $200

        
"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[function.get_exchange_rate, function.get_stock_price],

)
