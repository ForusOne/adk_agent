import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import VertexAiSearchTool

load_dotenv()

data_store_id = f"projects/{os.getenv('PROJECT_NUM')}/locations/{os.getenv('LOCATION')}/collections/default_collection/dataStores/{os.getenv('DATASTORE_ID')}"

print("Vertex AI Search data_store_id:", data_store_id)

vertex_search_tool = VertexAiSearchTool(data_store_id=data_store_id)

INSTRUCTION = """
    당신은 사용자의 질문에 대한 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면, 그 질문에 대한 'vertex_search_tool'에서 수행하고,그 결과를 바탕으로 답변을 제공해야 합니다.
    답변을 할 때는 아래와 같은 형식을 따라야 합니다.

    1. 질문: [질문 내용]
    2. 출처 정보 : [출처 이름]
    3. 답변: [답변 내용]
    4. 추가 정보: [추가 정보 내용]

"""


vertexai_search = Agent(
    name = "vertexai_search",
    model = os.getenv("MODEL"),
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[vertex_search_tool],
)

root_agent = vertexai_search