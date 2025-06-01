# ADK Parallel Workflow Agent

This folder demonstrates how to build and operate a parallel workflow agent using the ADK (Agent Development Kit) framework. The agent is designed to answer user questions by running positive and negative critique sub-agents in parallel, then summarizing the results with a review agent in a sequential pipeline.

## Overview

The Parallel Workflow Agent is designed to:
- Run positive and negative critique sub-agents in parallel to gather diverse perspectives
- Summarize and conclude based on the results of the parallel critiques using a review agent
- Use the language of the user's input for all responses
- Demonstrate modular agent design using ADK's parallel and sequential agent architecture

## Parallel agent

![Parallel agent](https://google.github.io/adk-docs/assets/parallel-agent.png)
Image source : https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents

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
adk/04-workflow/parallel/
├── __init__.py
├── agent.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the main workflow agent, combining parallel and sequential agents to orchestrate positive/negative critique and review steps.
- `sub_agent.py`  
  Implements the sub-agents for positive critique, negative critique, and review, each with their own instructions and response style.
- `__init__.py`  
  Marks the folder as a Python package.

## Agent Details (`agent.py`)

- Uses `ParallelAgent` to run `positive_critic` and `negative_critic` sub-agents in parallel
- Uses `SequentialAgent` to orchestrate the workflow: (parallel critiques) → review
- Returns a single agent ready to process user queries through this parallel and sequential workflow

## Sub-Agents (`sub_agent.py`)

- **`positive_critic`**
  - Writes a concise, clear positive review on a given topic
  - Always starts with "positive review."
  - Responds in the user's language
- **`negative_critic`**
  - Writes a concise, clear negative review on a given topic
  - Always starts with "negative review."
  - Responds in the user's language
- **`review_critic`**
  - Summarizes the positive and negative critiques and provides a final summary
  - Responds in the user's language


## Example Usage
Note : Execute the following command on **04-workflow** folder. 

```
ai_agent/adk/04-workflow $ adk web
```


## License

This project is licensed under the Apache License 2.0.
