import os
from dotenv import load_dotenv
from google.adk.agents import SequentialAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.

    1. 사용자가 질문을 입력하면, 먼저 그 질문의도를 정리해야 합니다. 다시에는 "질문의도" 라고 말하고, 그 질문의도를 정리합니다.

    2. 사용자의 질문에 대해서 반드시 아래와 같이 3가지 sub_agents 사용하여 답변을 제공해야 합니다.
        1. positive_critic 에이전트를 사용하여 긍정적인 비평을 답변합니다.
        2. negative_critic 에이전트를 사용하여 부정적인 비평을 답변합니다.
        3. review_critic 에이전트를 사용하여 전체적인 요약 및 결론을 답변합니다.
"""


pipeline_agent = SequentialAgent(
    name="pipeline_agent",
    sub_agents=[positive_critic, negative_critic, review_critic],
    description="Executes a sequence of positive_critic, negative_critic, and review_critic.",
)

root_agent = pipeline_agent
