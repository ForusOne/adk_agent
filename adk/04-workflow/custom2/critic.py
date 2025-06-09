# Copyright 2025 Forusone(forusone777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import AsyncGenerator
from typing_extensions import override

from google.adk.agents import LlmAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext

from google.adk.events import Event

class CriticAgent(BaseAgent):

    positive_critic_agent: LlmAgent
    negative_critic_agent: LlmAgent

    # model_config allows setting Pydantic configurations if needed, e.g., arbitrary_types_allowed
    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        positive_critic_agent: LlmAgent,
        negative_critic_agent: LlmAgent,
    ):
        # Initialize the PositiveAgent with sub-agents for critique
        super().__init__(
            name=name,
            positive_critic_agent=positive_critic_agent,
            negative_critic_agent=negative_critic_agent,
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:

        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):

            print(f"[{self.name}] Event from positive_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # yield an event and move on to the next step

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from negative_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # yield an event and move on to the next step

