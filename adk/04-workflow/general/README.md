# ADK General Workflow Agent

This folder demonstrates how to build and operate a general workflow agent using the ADK (Agent Development Kit) framework. The agent is designed to answer user questions by delegating critique tasks to sub-agents for positive and negative reviews, and to organize the intent of the user's question before providing a response.

---

## Overview

The General Workflow Agent is designed to:
- Organize and state the intent of the user's question
- Provide positive and/or negative critiques by delegating to sub-agents
- Use the language of the user's input for all responses
- Demonstrate modular agent design using ADK's sub-agent architecture

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
adk/04-workflow/general/
├── __init__.py
├── agent.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the main agent, its instruction template, and integrates sub-agents for positive and negative critique.
- `sub_agent.py`  
  Implements the `positive_critic` and `negative_critic` sub-agents, each with their own instructions and response style.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Integrates sub-agents for positive and negative critique
- Instruction flow:
  1. Organize and state the intent of the user's question
  2. Use the appropriate sub-agent(s) for positive and/or negative critique
- Supports:
  - Only positive critique (via `positive_critic`)
  - Only negative critique (via `negative_critic`)
  - Both critiques (invokes both sub-agents)

---

## Sub-Agents (`sub_agent.py`)

- **`positive_critic`**
  - Writes a concise, clear positive review on a given topic
  - Always starts with "positive review."
  - Responds in the user's language
- **`negative_critic`**
  - Writes a concise, clear negative review on a given topic
  - Always starts with "negative review."
  - Responds in the user's language


---
## Example Usage
Note : Execute the following command on **04-workflow** folder. 

```
ai_agent/adk/04-workflow $ adk web
```

---

## License

This project is licensed under the Apache License 2.0.
