# ADK Built-in Google Search Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with built-in Google Search capabilities. The agent can answer user queries by leveraging both its own knowledge and real-time search results, and formats responses with source information.

The Google Search Agent is designed to:
- Accept user questions on any topic
- Perform a Google search using the built-in tool
- Return a structured response including the question, search sources, and the answer
- Respond in the same language as the user's input

---

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools`). Example:

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

---

## Folder Structure

```
adk/03-tools/built-in/google_search/
├── __init__.py
├── agent.py
├── README.md
```

- `agent.py`  
  Defines the Google Search agent, its instruction template, and integrates the built-in Google Search tool.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Example Workflow

1. User asks a question (e.g., "What is the tallest building in the world?")
2. Agent performs a Google search for the question
3. Agent returns:
   - The original question
   - The search sources used
   - The answer based on the search results

---


## Example Usage
Note : Execute the following command on **03-tools/built-in** folder. 

```
ai_agent/adk/03-tools/built-in$ adk web
```


## License

This project is licensed under the Apache License 2.0.
