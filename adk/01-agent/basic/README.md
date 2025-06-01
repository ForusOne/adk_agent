
# ADK Basic Agent Example

This folder demonstrates how to build and operate a simple AI agent using the ADK (Agent Development Kit) framework.

## Overview

The `basic` agent is a minimal example that shows how to:
- Define an agent with a custom instruction and description
- Load environment variables for configuration
- Instantiate and return an ADK `Agent` object
- Run the agent to answer user queries in a structured format

## File Structure
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`  
  Contains the code to build and configure the basic agent.
- `__init__.py`  
  Marks the folder as a Python package.

## .env

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklK--------WYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "9215---43942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

## Execution
Note : Execute the following command on **01-agent** folder. 

```
ai_agent/adk/01-agent$ adk web
```

