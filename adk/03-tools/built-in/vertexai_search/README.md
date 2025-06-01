# ADK Built-in Vertex AI Search Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with Vertex AI Search integration. The agent can answer user queries by searching a specified Vertex AI Search data store and returning structured answers with source information.

The Vertex AI Search Agent is designed to:
- Accept user questions on any topic
- Perform a search using a specified Vertex AI Search data store
- Return a structured response including the question, source information, and the answer
- Respond in the same language as the user's input

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools/`).  

*** Note : Generally, if you didn't specify the region, GOOGLE_CLOUD_LOCATION, LOCATION should be global. ***

Example:

```
MODEL=your-model-name
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=global

PROJECT_ID = your-gcp-project-id
LOCATION = global

PROJECT_NUMBER=your-gcp-project-number
DATASTORE_ID=your-vertexai-datastore-id
```

---

## Folder Structure

```
adk/03-tools/built-in/vertexai_search/
├── __init__.py
├── agent.py
├── README.md
```

- `agent.py`  
  Defines the Vertex AI Search agent, its instruction template, and integrates the Vertex AI Search tool with dynamic configuration from environment variables.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Agent Details (`agent.py`)

- Loads environment variables (model name, project info, data store ID) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Integrates the `VertexAiSearchTool` from `google.adk.tools`
- Tool configuration:
  - Dynamically builds the data store resource path from environment variables
  - Initializes the Vertex AI environment for the correct project/location
- Instruction flow:
  - For each user question, perform a search using the Vertex AI Search tool
  - Format answers with question, source information, and answer
  - Always respond in the user's language

---

## Example Usage
Note : Execute the following command on **03-tools/built-in** folder. 

```
ai_agent/adk/03-tools/built-in$ adk web
```

## License

This project is licensed under the Apache License 2.0.
