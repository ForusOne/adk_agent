# A2A Basic Concept Example

This folder demonstrates a minimal working example of the A2A (Agent-to-Agent) protocol using Python. It includes a simple echo agent, a server to host the agent, and a client to interact with the agent using both streaming and non-streaming message APIs.
---

## Overview

This example shows how to:
- Define a simple agent that processes user input (echoes in uppercase)
- Expose the agent via an HTTP server using the A2A protocol
- Interact with the agent using a Python client (with streaming and non-streaming support)
- Demonstrate the A2A agent card and skill registration

---

## Folder Structure

```
a2a/concept/basic/
├── __init__.py
├── client.py
├── executor.py
├── server.py
├── README.md
```

- `client.py`  
  Asynchronous client that fetches the agent card, initializes an `A2AClient`, and sends user messages to the agent. Supports both streaming and non-streaming message APIs.
- `executor.py`  
  Implements the `EchoAgent` (which returns the user's query in uppercase) and the `EchoAgentExecutor` (which manages agent invocation and event queuing).
- `server.py`  
  Sets up and runs an A2A server using `A2AStarletteApplication`, exposing the echo agent via HTTP. Defines the agent's card, skills, and capabilities.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details (`executor.py`)

- **`EchoAgent`**: Simple agent that returns the user's query in uppercase.
- **`EchoAgentExecutor`**: Handles agent invocation, event queuing, and error handling for unsupported operations.

---

## Server Details (`server.py`)

- Defines the agent's skill and card (metadata, capabilities, supported modes)
- Uses `A2AStarletteApplication` and `Uvicorn` to serve the agent on `http://localhost:7777/`
- Handles incoming requests and delegates to the `EchoAgentExecutor`

---

## Client Details (`client.py`)

- Fetches the agent card from the server
- Initializes an `A2AClient` for communication
- Accepts user input and sends messages to the agent
- Prints both streaming and non-streaming responses from the agent

---

## Example Usage
### 1. install package
uv add python-a2a : https://pypi.org/project/python-a2a
uv add a2a-sdk : https://pypi.org/project/a2a-sdk

### 2. start server
```
/ai_agent/a2a/concept$ uv run -m basic.server
```
### 3. start client
```
(a2a) /ai_agent/a2a/concept$ uv run -m basic.client
```
### 4. check agent card.

```
curl http://0.0.0.0:7777/.well-known/agent.json
```

---

## License

This project is licensed under the Apache License 2.0.
