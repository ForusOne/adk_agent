# ADK MCP Server Exchange Rate Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent that uses the Model Context Protocol (MCP) to interact with a custom exchange rate server. The agent retrieves up-to-date exchange rate information by connecting to an MCP server that exposes an exchange rate tool implemented in Python.

The MCP Server Exchange Rate Agent is designed to:
- Help users retrieve exchange rate information between currencies
- Use the Model Context Protocol (MCP) to connect to a custom Python server exposing the `get_exchange_rate` tool
- Perform tool calls via MCP for up-to-date financial data
- Respond in the same language as the user's input

---

## check npx, adk
    ```    
    which npx
    which adk
    ```

    if there is no npx, install the node js.
    download file https://nodejs.org/en and install node-v22.16.0.pkg

---

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

```

## Folder Structure

```
adk/03-tools/mcp/server_exchange_rate/
├── __init__.py
├── agent.py
├── exchange_rate_server.py
├── README.md
```

- `agent.py`  
  Defines the agent, its instruction template, and integrates the MCPToolset for exchange rate operations via MCP.
- `exchange_rate_server.py`  
  Implements the MCP server that exposes the `get_exchange_rate` tool, handles tool listing and invocation, and runs over stdio for integration with ADK agents.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `LlmAgent` class from `google.adk.agents`
- Integrates the `MCPToolset` from `google.adk.tools.mcp_tool.mcp_toolset`
- MCP server is launched via `python3 -m server_exchange_rate.exchange_rate_server`
- Instruction flow:
  - For each user question, use the exchange rate tool to retrieve the requested information
  - Always respond in the user's language

---

## MCP Exchange Rate Server (`exchange_rate_server.py`)

- Implements the `get_exchange_rate` function using the Frankfurter API
- Exposes the function as an ADK FunctionTool and MCP tool
- Handles tool listing and invocation via MCP protocol
- Runs as a stdio server for integration with ADK agents

---
## Example Usage
Note : Execute the following command on **03-tools/mcp/ ** folder. 

```
ai_agent/adk/03-tools/mcp $ adk web
```

question : Show the exchange rate between Korean Won and US dollar.

---

## License

This project is licensed under the Apache License 2.0.
