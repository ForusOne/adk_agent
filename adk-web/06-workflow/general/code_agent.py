from google.adk.agents import LlmAgent
from . import prompt

code_agent = LlmAgent(
    name = "code_agent",
    model = "gemini-2.0-flash",
    description = "사용자의 질문에 대한 코드를 작성하고 실행한 후 답변하는 에이전트",
    instruction = prompt.CODE_AGENT_INSTRUCTION,
)