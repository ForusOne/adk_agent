# ADK Agent Callback Example

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with pre- and post-processing callbacks. The agent can intercept and modify the flow before and after the main agent logic runs, allowing for advanced control, custom responses, and state-based logic.

---

## Overview

The Agent Callback Example is designed to:
- Allow pre-processing before the agent runs (e.g., skip agent execution based on state)
- Allow post-processing after the agent runs (e.g., override or halt response based on state)
- Enable custom, state-driven conversational flows
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
adk/05-callback/agent_callback/
├── __init__.py
├── agent.py
├── callback.py
├── README.md
```

- `agent.py`  
  Defines the main agent, its instruction template, and attaches before/after callbacks for advanced control.
- `callback.py`  
  Implements the `callback_before_agent` and `callback_after_agent` functions, which can intercept and modify agent execution based on the session state.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Attaches `before_agent_callback` and `after_agent_callback` for advanced control
- Instruction flow:
  - For each user question, respond concisely and clearly in a structured format:
    - Question content
    - Question intent
    - Answer content
  - For casual conversation, answer naturally without special formatting

---

## Callback Functions (`callback.py`)

- **`callback_before_agent`**
  - Checks the session state for `skip_agent`. If set, skips agent execution and returns a custom response.
  - Otherwise, allows normal agent execution.
- **`callback_after_agent`**
  - Checks the session state for `check_response`. If set, returns a custom response and halts further processing.
  - Otherwise, allows normal agent execution.

---

## Example Workflow

1. User asks a question
2. If `skip_agent` is set in the state, the agent is skipped and a custom message is returned
3. If `check_response` is set in the state after agent execution, a custom message is returned
4. Otherwise, the agent responds normally

---
## Example Usage
Note : Execute the following command on **05-callback** folder. 

```
ai_agent/adk/05-callback $ uv run -m agent_callback.runner --command skip_llm_agent --query 'Explain about Generative AI'

ai_agent/adk/05-callback $ uv run -m agent_callback.runner --command check_response --query 'Explain about Generative AI'

```

---

## License

This project is licensed under the Apache License 2.0.
