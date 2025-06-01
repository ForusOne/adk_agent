# ADK State Conversation Agent - State

This folder demonstrates how to build and operate a conversational AI agent with explicit state management using the ADK (Agent Development Kit) framework. The agent can answer user queries, track state across turns, and supports explicit state changes via the ADK event system.

The State Conversation Agent is designed to:
- Answer user questions using real-time Google Search
- Track and update state across conversation turns
- Demonstrate both implicit (via `output_key`) and explicit (via events) state management

---

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
adk/02-conversations/state/
├── __init__.py
├── agent.py
├── output_key.py
├── state_change.py
├── README.md
```

- `agent.py`  
  Defines the agent, including its instruction template, Google Search tool integration, and a custom `output_key` for state tracking.
- `output_key.py`  
  Provides a script to run the agent in a conversational loop, displaying the session state after each turn to show how the agent's state evolves.
- `state_change.py`  
  Demonstrates explicit state changes using the ADK event system, including how to append system events and update session state (e.g., adding a timestamp).
- `__init__.py`  
  Marks the folder as a Python package.

---

## State Tracking Example (`output_key.py`)

- Runs the agent in a conversational loop
- After each user turn, prints the updated session state to show how the agent's state evolves
- Useful for debugging and understanding stateful agent behavior

#### Example Usage
```
uv run -m state.output_key --app_name search --user_id forus --session_id 1212
```

---

## Explicit State Change Example (`state_change.py`)

- Demonstrates how to append a system event to update the session state (e.g., adding a timestamp)
- Prints the state before and after the event to illustrate explicit state management

#### Example Usage
```
uv run -m state.state_change --app_name search --user_id forus --session_id 1212
```
---

## License

This project is licensed under the Apache License 2.0.
