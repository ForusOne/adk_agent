
from google.adk.agents import Agent

from . import prompt
from general.code_agent import code_agent
from general.search_agent import search_agent

root_agent = Agent(
    name = "root_agent",
    model = "gemini-2.0-flash",
    description = "사용자의 질문에 대해서 code_agent 나 search_agent를 통해 답변하는 에이전트",
    instruction = prompt.ROOT_AGENT_INSTRUCTION,
    sub_agents= [code_agent, search_agent],
)