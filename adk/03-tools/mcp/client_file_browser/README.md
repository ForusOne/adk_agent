# ADK MCP Client File Browser Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent that uses the Model Context Protocol (MCP) to interact with the file system. The agent can browse, read, and manage files in a specified folder by connecting to an MCP server using the `@modelcontextprotocol/server-filesystem` package.

The MCP Client File Browser Agent is designed to:
- Help users manage and browse files in a specified folder
- Use the Model Context Protocol (MCP) to connect to a file system server
- Perform file operations such as listing directories and reading files
- Respond in the same language as the user's input

## check npx, adk
    ```    
    which npx
    which adk
    ```

    if there is no npx, install the node js.
    download file https://nodejs.org/en and install node-v22.16.0.pkg

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
adk/03-tools/mcp/client_file_browser/
├── __init__.py
├── agent.py
├── README.md
```

- `agent.py`  
  Defines the agent, its instruction template, and integrates the MCPToolset for file system operations via MCP.
- `__init__.py`  
  Marks the folder as a Python package.

---


## Agent Details (`agent.py`)

- Loads environment variables (e.g., model name) using `dotenv`
- Uses the `LlmAgent` class from `google.adk.agents`
- Integrates the `MCPToolset` from `google.adk.tools.mcp_tool.mcp_toolset`
- MCP server is launched via `npx @modelcontextprotocol/server-filesystem` and connects to the specified folder
- Tool configuration:
  - The `target_folder_path` is set to the directory where the agent is running (can be customized)
  - Optional: You can filter which tools from the MCP server are exposed (e.g., `list_directory`, `read_file`)
- Instruction flow:
  - For each user question, use the file system toolset to perform the requested operation
  - Always respond in the user's language

---

## Example Workflow

1. User asks to list files in a folder or read a file
2. Agent uses the MCPToolset to connect to the file system via MCP
3. Agent performs the requested operation and returns the result

---

## Example Usage
Note : Execute the following command on **03-tools/mcp/ ** folder. 

```
ai_agent/adk/03-tools/mcp $ adk web
```

question : List up file in client_file_browser

---

## License

This project is licensed under the Apache License 2.0.
