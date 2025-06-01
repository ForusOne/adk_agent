# ADK Loop Workflow Agent

This folder demonstrates how to build and operate a multi-step, iterative workflow agent using the ADK (Agent Development Kit) framework. The agent uses a combination of sequential and loop agents to research, critique, refine, and summarize answers, supporting iterative improvement and review.

---

## Overview

The Loop Workflow Agent is designed to:
- Research a topic and generate an initial answer
- Iteratively critique and refine the answer up to a maximum number of times (loop)
- Exit the loop early if the answer is deemed satisfactory
- Summarize and conclude based on the final answer and critiques
- Use the language of the user's input for all responses

## Loop agent

![Loop agent](https://google.github.io/adk-docs/assets/loop-agent.png)
Image source : https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/#loop-agents

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

## Folder Structure

```
adk/04-workflow/loop/
├── __init__.py
├── agent.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the main workflow agent, combining sequential and loop agents to orchestrate research, critique, refinement, and conclusion steps.
- `sub_agent.py`  
  Implements the sub-agents for research, critique, refinement, and conclusion, as well as the loop exit tool.
- `__init__.py`  
  Marks the folder as a Python package.


## Agent Details (`agent.py`)

- Uses `LoopAgent` to perform iterative critique and refinement (up to 3 iterations)
- Uses `SequentialAgent` to orchestrate the workflow: research → (critique/refine loop) → conclusion
- Returns a single agent ready to process user queries through this multi-step workflow

## Sub-Agents and Tools (`sub_agent.py`)

- **`research_agent`**: Generates an initial review (positive and negative aspects) of a topic
- **`critic_agent`**: Critiques the answer, providing actionable feedback or confirming if no major issues are found
- **`refine_agent`**: Refines the answer based on critique; can call the `exit_loop` tool to break the loop if the answer is satisfactory
- **`conclusion_agent`**: Summarizes the final answer and critiques, providing a final summary
- **`exit_loop` tool**: Allows the loop to exit early if the answer is deemed complete


## Example Workflow

1. User asks a question
2. `research_agent` generates an initial answer
3. The agent enters a loop:
    - `critic_agent` critiques the answer
    - `refine_agent` refines the answer or calls `exit_loop` if complete
    - Loop continues up to 3 times or until `exit_loop` is called
4. `conclusion_agent` summarizes the final answer and critiques

---
## Example Usage
Note : Execute the following command on **04-workflow** folder. 

```
ai_agent/adk/04-workflow $ adk web
```

## License

This project is licensed under the Apache License 2.0.
