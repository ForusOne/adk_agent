# ADK Function Tool Multiple Call Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent that can call multiple function tools to answer user queries about exchange rates and stock prices. The agent uses external APIs to retrieve real-time financial data and formats responses according to user requests.

The Multiple Call Function Agent is designed to:
- Accept user queries about exchange rates and stock prices
- Call the appropriate function tool to retrieve real-time data
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
adk/03-tools/function/multiple_call/
├── __init__.py
├── agent.py
├── function.py
├── README.md
```

- `agent.py`  
  Defines the agent, its instruction template, and integrates function tools for exchange rate and stock price retrieval.
- `function.py`  
  Implements the `get_exchange_rate` and `get_stock_price` functions, which call external APIs to fetch financial data.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `Agent` class from `google.adk.agents`
- Integrates two function tools:
  - `get_exchange_rate`: Retrieves exchange rate information using the Frankfurter API
  - `get_stock_price`: Retrieves stock price information using the Alphavantage API
- Instruction flow:
  - For exchange rate queries, extract currencies and date, call `get_exchange_rate`, and format the answer
  - For stock queries, extract the symbol, call `get_stock_price`, and format the answer
  - Always respond in the user's language

---

## Function Tools (`function.py`)

- **`get_exchange_rate`**
  - Calls the Frankfurter API to get exchange rates between two currencies for a given date
  - Returns a dictionary with the exchange rate information
- **`get_stock_price`**
  - Calls the Alphavantage API to get the latest stock price for a given symbol
  - Returns a dictionary with the stock price information

---

## Example Workflow

1. User asks for an exchange rate (e.g., "What is the USD to KRW rate on 2025-05-20?")
2. Agent extracts the currencies and date, calls `get_exchange_rate`, and returns the formatted result
3. User asks for a stock price (e.g., "What is the price of Google stock today?")
4. Agent extracts the symbol, calls `get_stock_price`, and returns the formatted result

---


## Example Usage
Note : Execute the following command on **03-tools/function** folder. 

```
ai_agent/adk/03-tools/function$ adk web
```

---


## License

This project is licensed under the Apache License 2.0.
