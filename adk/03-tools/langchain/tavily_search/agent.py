import os
from dotenv import load_dotenv
from google.adk.agents import Agent

from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

from . import function

load_dotenv()

# Instantiate the LangChain tool
tavily_tool_instance = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

# Wrap it with LangchainTool for ADK
adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)

INSTRUCTION = """ 당신은 환율 정보와 경제 상황에 대해서 검색 후 답해주는 AI Agent 입니다.

    1. 다양한 경제상황에 대한 정보를 'adk_tavily_tool' 툴을 통해서 검색해서 답변해주세요.

    2. 환율정보는 'get_exchange_rate' 툴을 통해서 알려주세요.
       날짜기준 환율과 변환대상 환율을 알려주면 해당 제시된 날짜기준의 환율정보를 알려주세요.
       환율정보에 대한 답변 형식은 아래와 같습니다.
        - 기준환율: USD
        - 변환대상환율: KRW
        - 날짜 : 2025-05-20
        - 환율 : 
"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[adk_tavily_tool, function.get_exchange_rate]
)
