import os
from dotenv import load_dotenv

from google.adk.agents import Agent

load_dotenv()

positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 긍적적인 측면을 답변하는 에이전트",
    instruction = """당신은 주어진 주제에 대해서 긍정적인 비평을 작성하는 에이전트입니다. 
                    사용자가 주제를 입력하면, 그 주제에 대한 긍정적인 면에 대한 검색을 통해서 긍정적인 비평을 작성해야 합니다. 
                    답을 제공할 때는 최대한 간결하고 명확하게 작성해야 하고, 서두에 "긍정적인 비평" 이라고 말해야 합니다.
                """,
)    

negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 부정적인 측면을 답변하는 에이전트",
    instruction = """당신은 주어진 주제에 대해서 부정적인 비평을 작성하는 에이전트입니다. 
                    사용자가 주제를 입력하면, 그 주제에 대한 부정적인 면에 대한 검색을 통해서 부정적인 비평을 작성해야 합니다. 
                    답을 제공할 때는 최대한 간결하고 명확하게 작성해야 하고, 서두에 "부정적인 비평" 이라고 말해야 합니다.
                """,
)    

review_critic = Agent(
    name = "review_critic",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 대해서 긍정적인 측면과 부정적인 측면을 통해서 결론을 정리해주는 Agent",
    instruction = """당신은 주어진 주제에 대해서 긍정적인 측면과 부정적인 비평을 바탕으로 최종 요약 및 결론을 설명하는 에이전트입니다. 
                    답변 시에 "설명 최종 요약" 이라고 말하고 답변해주세요. 
                """,
)   
