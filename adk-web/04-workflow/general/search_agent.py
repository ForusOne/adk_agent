from google.adk.agents import LlmAgent
from . import prompt

search_agent = LlmAgent(
    name = "search_agent",
    model = "gemini-2.0-flash",
    description = "사용자의 질문에 답변 하는 에이전트",
    instruction = prompt.SEARCH_AGENT_INSTRUCTION,
)