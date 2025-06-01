# ADK Output Schema Example

This folder demonstrates how to define and enforce structured output schemas for agent responses using the Agent Development Kit (ADK). It includes an agent that produces answers in a strict schema format, leveraging Pydantic for schema validation.
---

## Overview

This example shows how to:
- Define a strict output schema for agent responses using Pydantic
- Instruct the agent to always follow the schema when answering questions
- Enforce output structure for downstream processing or integration

---

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"

```
---
## Folder Structure

```
adk/08-output/schema/
├── agent.py
├── schema.py
├── __init__.py
├── README.md
```

- `agent.py`  
  Defines the main agent, its instruction template, and attaches the output schema for structured responses.
- `schema.py`  
  Implements the `SearchResult` Pydantic model, which specifies the required output format for the agent's answers.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Output Schema Details (`schema.py`)

- **`SearchResult`** (Pydantic model):
  - `query` (str): The user's query string
  - `intention` (str): The user's intention or purpose for asking the query
  - `result` (str): The results or answer corresponding to the query
- The schema is referenced in the agent's configuration to ensure all outputs match this structure.
- Example JSON schema:
  ```json
  {
    "title": "search_results",
    "type": "OBJECT",
    "description": "search results",
    "required": ["query", "intention", "result"],
    "properties": {
      "query": {"title": "query", "type": "STRING", "description": "user's query"},
      "intention": {"title": "intention", "type": "STRING", "description": "user's intention to ask"},
      "result": {"title": "result", "type": "STRING", "description": "results"}
    },
    "property_ordering": ["query", "intention", "result"]
  }
  ```

---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Attaches the `SearchResult` output schema to enforce structured answers
- Instruction flow:
  - For each user question, respond using the exact output schema
  - Always use the same language as the user's question

---
## Example Usage
Note : Execute the following command on **08-output** folder. 

```
ai_agent/adk/08-output $ adk web
```
---

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/08-output/`). Example:
```
MODEL=your-model-name
```

---

## License

This project is licensed under the Apache License 2.0.
