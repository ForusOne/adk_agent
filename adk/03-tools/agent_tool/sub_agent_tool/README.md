# ADK Agent Tool with Sub-Agent Critique Example

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent that delegates critique tasks to sub-agents using the AgentTool interface. The root agent can provide positive and/or negative critiques by invoking specialized sub-agents as tools.

The Sub-Agent Tool Critique Agent is designed to:
- Organize the user's question intent
- Provide positive and/or negative critiques by delegating to sub-agents
- Use the language of the user's input for all responses
- Demonstrate modular agent design using the ADK's AgentTool interface

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools/`). Example:

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
adk/03-tools/agent_tool/sub_agent_tool/
├── __init__.py
├── agent.py
├── sub_agent.py
└── README.md
```

- `agent.py`  
  Defines the root agent, its instruction template, and attaches sub-agent tools for positive and negative critique.
- `sub_agent.py`  
  Defines the `positive_critic` and `negative_critic` sub-agents, each with their own instructions and response style.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Example Workflow

1. User asks for a critique (positive, negative, or both) on a topic
2. Root agent organizes the question intent
3. Root agent invokes the appropriate sub-agent tool(s)
4. Sub-agents generate the requested critiques
5. Root agent returns the combined response to the user

---

## Example Usage
Note : Execute the following command on **03-tools/agent_tool** folder. 

```
ai_agent/adk/03-tools/agent_tool$ adk web
```

---

## License

This project is licensed under the Apache License 2.0.
