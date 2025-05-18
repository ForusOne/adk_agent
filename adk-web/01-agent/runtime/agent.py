import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agent import positive_critic, negative_critic

load_dotenv()

INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    아래와 같은 흐름으로 답변을 해주세요. 

    1. 사용자가 질문을 입력하면, 먼저 그 질문의도를 정리해야 합니다. 다시에는 "질문의도" 라고 말하고, 그 질문의도를 정리합니다.

    2. 사용자의 질문에 따라서 아래와 같이 sub_agents 사용하여 답변을 제공해야 합니다.
        1. 사용자가 긍정적인 비평을 요청하면, positive_critic 에이전트를 사용하여 긍정적인 비평을 작성합니다.
        2. 사용자가 부정적인 비평을 요청하면, negative_critic 에이전트를 사용하여 부정적인 비평을 작성합니다.
        3. 사용자가 긍정적인 비평과 부정적인 비평을 모두 요청하면, 두 에이전트(positive_critic, negative_critic) 를 모두 사용하여 각각의 비평을 작성합니다.
    
"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    sub_agents = [positive_critic, negative_critic],
)

root_agent_tool = Agent(
    name = "root_agent_tool",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools = [AgentTool(agent=positive_critic),AgentTool(agent=negative_critic)]
)

# root_agent = root_agent_tool