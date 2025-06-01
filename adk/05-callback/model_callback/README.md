# ADK Model Callback Example

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with pre- and post-processing callbacks at the model (LLM) level. The agent can intercept and modify the flow before and after the LLM model is called, allowing for advanced control, keyword filtering, and state-based logic.

---

## Overview

The Model Callback Example is designed to:
- Allow pre-processing before the LLM model is called (e.g., block LLM calls based on keywords in user input)
- Allow post-processing after the LLM model generates a response (e.g., block or modify responses based on keywords in the output)
- Enable custom, state-driven conversational flows and content moderation
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
adk/05-callback/model_callback/
├── __init__.py
├── agent.py
├── callback.py
├── README.md
```

- `agent.py`  
  Defines the main agent, its instruction template, and attaches before/after model callbacks for advanced control.
- `callback.py`  
  Implements the `callback_before_model` and `callback_after_model` functions, which can intercept and modify LLM execution based on the session state and model response.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Attaches `before_model_callback` and `after_model_callback` for advanced control
- Instruction flow:
  - For each user question, respond concisely and clearly in a structured format:
    - Question content
    - Question intent
    - Answer content
  - For casual conversation, answer naturally without special formatting

---

## Callback Functions (`callback.py`)

- **`callback_before_model`**
  - Checks the session state for a `keyword`. If the keyword is found in the user's query, blocks the LLM call and returns a custom message.
  - Otherwise, allows the LLM call to proceed.
- **`callback_after_model`**
  - Checks the session state for a `keyword`. If the keyword is found in the LLM response, blocks the response and returns a custom message.
  - Otherwise, allows the response to proceed as normal.

---

## Example Workflow

1. User asks a question
2. If the `keyword` is found in the user's query, the LLM call is blocked and a custom message is returned
3. If the `keyword` is found in the LLM response, the response is blocked and a custom message is returned
4. Otherwise, the agent responds normally

---
## Example Usage
Note : Execute the following command on **05-callback** folder. 

```
ai_agent/adk/05-callback $ uv run -m model_callback.runner --keyword violent --query 'What is the violent crime?'

ai_agent/adk/05-callback $ uv run -m model_callback.runner --keyword election --query 'What is the way to become a president?'

```
---

## License

This project is licensed under the Apache License 2.0.
