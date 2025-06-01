
# ADK MCP Tools Overview

This directory contains examples of ADK (Agent Development Kit) agents that use the Model Context Protocol (MCP) to interact with external systems such as file systems and custom servers. Each subfolder demonstrates a different approach to using MCP-powered tools within ADK agents.

---

## Subfolders Overview

### 1. `client_file_browser/` — MCP Client File Browser Agent
- Helps users manage and browse files in a specified folder using MCP.
- Connects to a file system server via `@modelcontextprotocol/server-filesystem`.
- See [`client_file_browser/README.md`](./client_file_browser/README.md) for details.

### 2. `server_exchange_rate/` — MCP Server Exchange Rate Agent
- Retrieves exchange rate information by connecting to a custom Python MCP server exposing the `get_exchange_rate` tool.
- Integrates a Python-based MCP server for up-to-date financial data.
- See [`server_exchange_rate/README.md`](./server_exchange_rate/README.md) for details.


---

## Getting Started

1. Choose a subfolder (`client_file_browser` or `server_exchange_rate`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.