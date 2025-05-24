import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools import ToolContext

load_dotenv()

RESEARCH_OUTCOME = "initial_sentence"
STATE_CRITICISM = "criticism"
COMPLETION_PHRASE = "No major issues found."

def exit_loop(tool_context: ToolContext):
  """Call this function ONLY when the critique indicates no further changes are needed, 
    signaling the iterative process should end."""
  
  print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  
  return {}

research_agent = Agent(
    name = "research_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 긍적적인 측면, 부정적인 측면을 답변하는 에이전트",
    instruction = """당신은 주어진 주제에 대해서 긍정적인 비평 및 부정적인 비평을 =작성하는 에이전트입니다. 
                    사용자가 주제를 입력하면, 그 주제에 대한 긍정적인 면 및 부정적인 비평에 대한 내용을 작성해야 합니다. 
                    답을 제공할 때는 최대한 간결하고 명확하게 작성해야 하고, 서두에 "비평 작성" 이라고 말해야 합니다.
                """,
    output_key="RESEARCH_OUTCOME"                
)    

critic_agent = Agent(
    name = "critic_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 대해서 긍정적인 측면과 부정적인 측면을 통해서 리뷰 정리해주는 Agent",
    instruction = f"""
                    당신은 사용자의 질문에 답변을 검토하는 건설적인 비평 AI Agent 입니다.
                    답변에 "## 답변 리뷰" 라는 제목을 추가하세요.

                    **검토할 문서:**
                    ```
                    {RESEARCH_OUTCOME}
                    ```

                    **작업:**
                    답변 내용을 아래와 같은 기준으로 명확하게 검토하세요.

                    답변을 더 나은 방향으로 개선할 수 있는 *명확하고 실행 가능한* 방법을 1~2가지 제시하세요.
                    반드시 우리 사회 및 조직에 미칠수 있는 내용이 들어가야 합니다.
                    다음과 같은 구체적인 제안을 간결하게 제시하세요. 비평 텍스트 *만* 출력하세요.

                    답변이 괜찮은 경우:
                    "{COMPLETION_PHRASE}"라는 문구만 *정확하게* 응답하고 다른 문구는 출력하거나 설명을 추가하지 마세요. 

                """,
    output_key=STATE_CRITICISM,                
)   

refine_agent = Agent(
    name = "refine_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 대해서 긍정적인 측면과 부정적인 측면을 통해서 리뷰 정리해주는 Agent",
    instruction = f"""
                    당신은 사용자의 질문에 답변을 검토하는 건설적인 비평 AI Agent 입니다.
                    응답에 "## 답변 검증 "이라는 제목을 추가하세요.

                    **현재 문서:**
                    ```
                    {RESEARCH_OUTCOME}
                    ```
                    **비평/제안:**
                    {STATE_CRITICISM}

                    **과제:**
                    '비평/제안'을 분석하세요.

                    비평이 *정확히* "{COMPLETION_PHRASE}"인 경우:
                    'exit_loop' 함수를 호출해야 합니다. 텍스트를 출력하지 마세요.
                    그렇지 않은 경우(비평에 실행 가능한 피드백이 포함된 경우):
                    '현재 문서'를 개선하기 위해 제안을 신중하게 적용하세요. 다듬어진 문서 텍스트 *만* 출력하세요.
                    설명을 추가하지 마세요. 다듬어진 문서를 출력하거나 exit_loop 함수를 호출하세요. """,
    tools=[exit_loop],

)   

conclusion_agent = Agent(
    name = "conclusion_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 대해서 긍정적인 측면과 부정적인 측면을 통해서 결론을 정리해주는 Agent",
    instruction = f"""당신은 주어진 주제에 대해서 긍정적인 측면과 부정적인 비평을 바탕으로 최종 요약 및 결론을 설명하는 에이전트입니다. 
                    답변 시에 아래 현재 문서와 비평/제안 부분을 참고해서 "최종 요약" 이라고 말하고 답변해주세요. 
                    
                    **현재 문서:**
                    ```
                    {RESEARCH_OUTCOME}
                    ```
                    **비평/제안:**
                    {STATE_CRITICISM}

                """,
)