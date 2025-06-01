# ADK Custom Workflow Critic Agent

This folder demonstrates how to build and operate a custom multi-stage critique agent using the Agent Development Kit (ADK). The agent orchestrates a workflow of positive, negative, and review critiques by delegating to specialized sub-agents and coordinating their outputs.

---

## Overview

The Custom Workflow Critic Agent is designed to:
- Accept user input on a topic
- Run a positive critique, then a negative critique, then a review/summary
- Yield events and outputs from each stage
- Abort the workflow early if required output conditions are not met (e.g., missing keywords in the state)
- Respond in the same language as the user's input

---

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "9215---43942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

---

## Folder Structure

```
adk/04-workflow/custom/
├── __init__.py
├── agent.py
├── critic.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the root CriticAgent, which coordinates the workflow using sub-agents for positive, negative, and review critiques.
- `critic.py`  
  Implements the `CriticAgent` class, a custom agent that runs a multi-step critique workflow, yielding events from each sub-agent and supporting conditional early termination.
- `sub_agent.py`  
  Defines the sub-agents:
    - `positive_critic_agent`: Generates positive reviews.
    - `negative_critic_agent`: Generates negative reviews.
    - `review_critic_agent`: Summarizes and concludes based on the previous critiques.
- `__init__.py`  
  Marks the folder as a Python package.


---

## Agent Details

### Root Agent (`agent.py`)
- Loads environment variables (e.g., model name) using `dotenv`
- Instantiates a `CriticAgent` with references to the three sub-agents
- The root agent is ready to process user queries and orchestrate the workflow

### CriticAgent (`critic.py`)
- Subclasses `BaseAgent` and coordinates the workflow using a `SequentialAgent` and the review agent
- Runs the positive and negative critics in sequence, then the review critic
- Checks for required keywords in the state after each step (e.g., "images" for positive, "social" for negative)
- Aborts the workflow if conditions are not met, otherwise yields all events

### Sub-Agents (`sub_agent.py`)
- **`positive_critic_agent`**: Writes a concise, clear positive review, outputting to `positive_critic_output`
- **`negative_critic_agent`**: Writes a concise, clear negative review, outputting to `negative_critic_output`
- **`review_critic_agent`**: Summarizes and concludes based on the previous critiques, outputting to `review_output`

---

## Example Workflow

1. User provides a topic for critique
2. The agent runs the positive critic and yields its output
3. If the output contains "images", proceeds to the negative critic; otherwise, aborts
4. The agent runs the negative critic and yields its output
5. If the output contains "social", proceeds to the review critic; otherwise, aborts
6. The agent runs the review critic and yields its output

---

## Example Usage
Note : Execute the following command on **04-workflow** folder. 

```
ai_agent/adk/04-workflow $ adk web
```

---

## License

This project is licensed under the Apache License 2.0.
