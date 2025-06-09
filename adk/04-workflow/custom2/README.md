# ADK Custom Workflow CriticAgent Example

This folder demonstrates how to build and operate a custom multi-stage critique agent using the Agent Development Kit (ADK). The agent orchestrates a workflow of positive and negative critiques by delegating to specialized sub-agents and coordinating their outputs.

---

## Overview

The Custom Workflow CriticAgent is designed to:
- Accept user input on a topic
- Run a positive critique, then a negative critique, yielding events from each stage
- Respond in the same language as the user's input
- Easily extend to more complex workflows by customizing the CriticAgent logic

---

## .env Sample

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKuZh6Bd8 

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

---

## Folder Structure

```
adk/04-workflow/custom2/
├── __init__.py
├── agent.py
├── critic.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the root `CriticAgent`, which coordinates the workflow using sub-agents for positive and negative critiques.
- `critic.py`  
  Implements the `CriticAgent` class, a custom agent that runs a multi-step critique workflow, yielding events from each sub-agent.
- `sub_agent.py`  
  Defines the sub-agents:
    - `positive_critic_agent`: Generates positive reviews.
    - `negative_critic_agent`: Generates negative reviews.
- `__init__.py`  
  Marks the folder as a Python package.

---

## How It Works

### Root Agent (`agent.py`)
- Loads environment variables (e.g., model name) using `dotenv`.
- Instantiates a `CriticAgent` with references to the two sub-agents.
- The root agent is ready to process user queries and orchestrate the workflow.

### CriticAgent (`critic.py`)
- Subclasses `BaseAgent` and coordinates the workflow.
- Runs the positive and negative critics in sequence.
- Yields all events from both sub-agents, allowing for streaming responses.
- Can be extended to add more workflow logic or conditional branching.

### Sub-Agents (`sub_agent.py`)
- **`positive_critic_agent`**: Writes a concise, clear positive review.
- **`negative_critic_agent`**: Writes a concise, clear negative review.

---

## How to Operate with ADK Framework

1. **Install dependencies**: Make sure you have the ADK and required packages installed (see `pyproject.toml`).
2. **Set up your `.env` file**: Place your model and API credentials in a `.env` file in the parent folder.
3. **Run the agent**: Use the ADK runner or web interface to start the agent. For example:
   ```bash
   ai_agent/adk/04-workflow $ adk web
   ```
4. **Interact with the agent**: Enter a topic for critique. The agent will respond with positive and negative reviews in sequence.

---

## License

This project is licensed under the Apache License 2.0.
