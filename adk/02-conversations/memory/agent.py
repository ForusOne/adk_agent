# Copyright 2025 Google LLC
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

import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import load_memory # Tool to query memory

load_dotenv()

SEARCH_INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면, 그 질문에 대한 구글 검색(google_search) 툴을 수행하고,그 결과를 바탕으로 답변을 제공해야 합니다.
    
    답변을 할 때는 아래와 같은 형식을 따라야 합니다.
    1. 질문: [질문 내용]
    2. 출처 정보 : [출처 이름]
    3. 답변: [답변 내용]
    4. 추가 정보: [추가 정보 내용]
"""

search_agent = Agent(
    name = "search_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 구글 검색 후 답변하는 에이전트",
    instruction = SEARCH_INSTRUCTION,
    tools=[google_search],
)

RECALL_INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    사용자가 질문하면 'load_memory' 툴을 사용하여 메모리를 조회하고, 그 결과를 바탕으로 답변을 제공해야 합니다.
    """

recall_agent = Agent(
    name = "search_agent",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 메모리에서 조회하여 답변하는 에이전트",
    instruction = RECALL_INSTRUCTION,
    tools=[load_memory],
)

