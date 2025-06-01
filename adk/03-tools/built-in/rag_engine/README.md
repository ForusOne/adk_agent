# ADK Built-in RAG Engine Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with built-in Retrieval-Augmented Generation (RAG) capabilities using Vertex AI. The agent can answer user queries by retrieving relevant documentation and reference materials from a RAG corpus, and formats responses with citations.

The RAG Engine Agent is designed to:
- Accept user questions on any topic
- Retrieve relevant documentation and reference materials from a Vertex AI RAG corpus
- Return a structured response including the question, citations, and the answer
- Respond in the same language as the user's input

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools/`). Example:

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools`). Example:

Note : This file should be located in the **parent upper folder**.

**GOOGLE_GENAI_USE_VERTEXAI=TRUE**
**RAG_CORPUS = "projects/ai-forus/locations/us-central1/ragCorpora/488021311111353728"**

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"

RAG_CORPUS = "projects/ai-forus/locations/us-central1/ragCorpora/488021311111353728"


```

```
google.genai.errors.ClientError: 401 UNAUTHENTICATED. {'error': {'code': 401, 'message': 'API keys are not supported by this API. Expected OAuth2 access token or other authentication credentials that assert a principal. See https://cloud.google.com/docs/authentication', 'status': 'UNAUTHENTICATED', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'CREDENTIALS_MISSING', 'domain': 'googleapis.com', 'metadata': {'service': 'aiplatform.googleapis.com', 'method': 'google.cloud.aiplatform.v1beta1.PredictionService.GenerateContent'}}]}}
```



## Folder Structure

```
adk/03-tools/built-in/rag_engine/
├── __init__.py
├── agent.py
├── README.md
```

- `agent.py`  
  Defines the RAG engine agent, its instruction template, and integrates the Vertex AI RAG retrieval tool.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name, RAG corpus) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Integrates the `VertexAiRagRetrieval` tool from `google.adk.tools.retrieval.vertex_ai_rag_retrieval`
- Tool configuration:
  - `rag_resources` is set to the RAG corpus specified by the `RAG_CORPUS` environment variable
  - `similarity_top_k` and `vector_distance_threshold` control retrieval precision
- Instruction flow:
  - For each user question, perform a RAG retrieval
  - Format answers as:
    1. Question:
    2. Citations:
    3. Answer:
  - Always respond in the user's language

---

## Example Workflow

1. User asks a question (e.g., "What is Vertex AI RAG?")
2. Agent retrieves relevant documentation from the RAG corpus
3. Agent returns:
   - The original question
   - Citations to the retrieved documents
   - The answer based on the retrieved content

---


## Example Usage
Note : Execute the following command on **03-tools/built-in** folder. 

```
ai_agent/adk/03-tools/built-in$ adk web
```

---


## License

This project is licensed under the Apache License 2.0.
