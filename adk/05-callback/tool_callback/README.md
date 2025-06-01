# ADK Tool Callback Example

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with pre- and post-processing callbacks at the tool level. The agent can intercept and modify the flow before and after a tool is called, allowing for advanced control, custom responses, and argument/result manipulation.
---

## Overview

The Tool Callback Example is designed to:
- Allow pre-processing before a tool runs (e.g., modify arguments, redirect tool calls)
- Allow post-processing after a tool runs (e.g., modify results, add notes)
- Enable custom, context-driven tool flows
- Respond in a structured format or handle casual conversation naturally

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
adk/05-callback/tool_callback/
├── __init__.py
├── agent.py
├── callback.py
├── runner.py
├── README.md
```

- `agent.py`  
  Defines the main agent, its instruction template, and attaches before/after tool callbacks for advanced control.
- `callback.py`  
  Implements the `get_capital_city` tool function, and the `callback_before_tool` and `callback_after_tool` functions, which can intercept and modify tool execution and results.
- `runner.py`  
  Provides an async runner to interact with the agent from the command line.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Attaches `callback_before_tool` and `callback_after_tool` for advanced tool-level control
- Instruction flow:
  - For each user question, respond concisely and clearly in a structured format:
    - Question content
    - Question intent
    - Answer content
  - For casual conversation, answer naturally without special formatting
- Registers the `get_capital_city` tool

---

## Tool & Callback Functions (`callback.py`)

- **`get_capital_city(country: str)`**
  - Returns the capital city for a given country from a predefined dictionary.
- **`callback_before_tool(tool, args, tool_context)`**
  - Intercepts tool calls. If the tool is `get_capital_city` and the country is 'Korea', it changes the argument to 'South Korea'.
  - Otherwise, passes the original arguments through.
- **`callback_after_tool(tool, args, tool_context, tool_response)`**
  - Intercepts tool results. If the tool is `get_capital_city` and the result is 'Seoul', it appends a note indicating it's the capital of South Korea.
  - Otherwise, passes the original result through.

---

## Example Workflow

1. User asks a question (e.g., "What is the capital city of Korea?")
2. The before-tool callback checks and modifies the argument if needed (e.g., 'Korea' → 'South Korea')
3. The tool runs and returns a result (e.g., 'Seoul')
4. The after-tool callback checks and modifies the result if needed (e.g., adds a note to 'Seoul')
5. The agent responds with the final answer

---
## Example Usage
Note : Execute the following command on **05-callback** folder. 

```
ai_agent/adk/05-callback $ uv run -m tool_callback.runner --query "what is the capital city of korea?"

ai_agent/adk/05-callback $ uv run -m tool_callback.runner --query 'what is the capital city of US?'

```
---

## License

This project is licensed under the Apache License 2.0.
