import os
from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import ParallelAgent
from google.adk.agents import LoopAgent

from .sub_agent import research_agent
from .sub_agent import critic_agent
from .sub_agent import refine_agent
from .sub_agent import conclusion_agent

load_dotenv()

critics_loop = LoopAgent(
    name="critics_loop",
    sub_agents=[
        critic_agent,
        refine_agent,
    ],
    max_iterations=3
)

confirmation_agent = SequentialAgent(
    name="confirmation_agent",
    sub_agents=[
        research_agent, 
        critics_loop,
        conclusion_agent
    ],
    description="Executes a sequence of research_agent and critics_loop.",
)

root_agent = confirmation_agent
