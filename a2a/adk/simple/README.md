# A2A ADK Simple Example

This folder demonstrates a simple integration of the Google ADK agent with the A2A (Agent-to-Agent) protocol. It provides a working example of how to expose an ADK-powered agent as an A2A-compliant service, and how to interact with it using a Python client.

---

## Overview

This example shows how to:
- Define an ADK agent that answers user questions using Google Search
- Expose the agent via an HTTP server using the A2A protocol
- Interact with the agent using a Python client (with streaming and non-streaming support)
- Convert message formats between A2A and GenAI for seamless integration

---
## .env

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
a2a/adk/simple/
├── __init__.py
├── agent.py
├── client.py
├── convert.py
├── executor.py
├── server.py
├── README.md
```

- `agent.py`  
  Defines the main ADK agent, its instruction template, and attaches the Google Search tool for answering user queries.
- `client.py`  
  Asynchronous client that fetches the agent card, initializes an `A2AClient`, and sends user messages to the agent. Supports both streaming and non-streaming message APIs.
- `convert.py`  
  Utility functions for converting message parts between A2A and Google GenAI formats.
- `executor.py`  
  Implements the `ADKAgentExecutor`, which manages the lifecycle of the ADK agent, session management, and event queue updates for A2A requests.
- `server.py`  
  Sets up and runs an A2A server using `A2AStarletteApplication`, exposing the ADK agent via HTTP. Defines the agent's card, skills, and capabilities.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details (`agent.py`)

- **ADK Agent**: Answers user questions using the Google Search tool. Follows a strict answer format:
  1. Question
  2. Source information
  3. Answer
- Uses the same language as the user's question.

---

## Server Details (`server.py`)

- Defines the agent's skill and card (metadata, capabilities, supported modes)
- Uses `A2AStarletteApplication` and `Uvicorn` to serve the agent on `http://localhost:7777/`
- Handles incoming requests and delegates to the `ADKAgentExecutor`

---

## Client Details (`client.py`)

- Fetches the agent card from the server
- Initializes an `A2AClient` for communication
- Accepts user input and sends messages to the agent
- Prints both streaming and non-streaming responses from the agent

---

## Conversion Utilities (`convert.py`)

- Converts message parts between A2A and Google GenAI formats for compatibility

---

## Example Usage

### 1. install package
uv add python-a2a : https://pypi.org/project/python-a2a
uv add a2a-sdk : https://pypi.org/project/a2a-sdk

### 2. start server
```
/ai_agent/a2a/adk$ uv run -m simple.server
```
### 3. start client
```
/ai_agent/a2a/adk$ uv run -m simple.client
```
### 4. check agent card.

```
curl http://0.0.0.0:7777/.well-known/agent.json
```

---

## License

This project is licensed under the Apache License 2.0.
