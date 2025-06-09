# ADK Event Conversation Agent - Event

This folder demonstrates how to build and operate an event-driven conversational AI agent using the ADK (Agent Development Kit) framework. The agent is designed to answer user queries by performing a Google search and providing structured responses, while the runner script showcases detailed event streaming and introspection.

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/02-conversations/`). Example:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

## Folder Structure

```
adk/02-conversations/event/
├── __init__.py
├── agent.py
├── runner.py
└── README.md
```

- `agent.py`  
  Defines the agent, including its instruction template and integration with the Google Search tool.
- `runner.py`  
  Provides an asynchronous script to run the agent, stream events, and print detailed event information for each step of the conversation.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Example Usage
Note : Execute the following command on **01-conversations** folder. 

```
ai_agent/adk/02-conversations$ uv run -m event.runner
```

# Event Conversation Example (ADK)

## Example Overview
This folder demonstrates how to use the ADK framework to build agents that manage event-driven conversations. The agent can process and respond to events in a conversational context.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
Run the event conversation agent with:

```bash
uv run python agent.py
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../../LICENSE) file for details.