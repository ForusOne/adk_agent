# ADK Function Tool Single Call Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent that can call a single function tool to answer user queries about exchange rates. The agent uses an external API to retrieve real-time exchange rate data and formats responses according to user requests.

The Single Call Function Agent is designed to:
- Accept user queries about exchange rates
- Call the function tool to retrieve real-time data
- Format answers in a structured, user-friendly way
- Respond in the same language as the user's input

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools/`).  

Example:

```

GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

MODEL=your-model-name
PROJECT_ID = your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION = us-central1

STOCK_API_KEY = "CBPHIOdfdGA890ZMA"

```

## Folder Structure

```
adk/03-tools/function/single_call/
├── __init__.py
├── agent.py
├── function.py
├── README.md
```

- `agent.py`  
  Defines the agent, its instruction template, and integrates a function tool for exchange rate retrieval.
- `function.py`  
  Implements the `get_exchange_rate` function, which calls an external API to fetch exchange rate data.
- `__init__.py`  
  Marks the folder as a Python package.

---


## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Integrates a single function tool:
  - `get_exchange_rate`: Retrieves exchange rate information using the Frankfurter API
- Instruction flow:
  - For exchange rate queries, extract currencies and date, call `get_exchange_rate`, and format the answer
  - Always respond in the user's language

---

## Function Tool (`function.py`)

- **`get_exchange_rate`**
  - Calls the Frankfurter API to get exchange rates between two currencies for a given date
  - Returns a dictionary with the exchange rate information

---

## Example Workflow

1. User asks for an exchange rate (e.g., "What is the USD to KRW rate on 2025-05-20?")
2. Agent extracts the currencies and date, calls `get_exchange_rate`, and returns the formatted result

---


## Example Usage
Note : Execute the following command on **03-tools/function** folder. 

```
ai_agent/adk/03-tools/function$ adk web
```

---


## License

This project is licensed under the Apache License 2.0.
