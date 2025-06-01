# ADK Tools Overview

This directory contains a comprehensive set of examples for integrating various types of tools into ADK (Agent Development Kit) agents. Each subfolder demonstrates a different approach to tool integration, including built-in tools, function tools, LangChain tools, and Model Context Protocol (MCP) tools. Use these examples to learn how to extend agent capabilities with real-world data, web search, code execution, and external system integration.

![tool flow](https://google.github.io/adk-docs/assets/quickstart-flow-tool.png)
Image source : https://google.github.io/adk-docs/get-started/quickstart/#create-agent-project

---

## Subfolders & Summaries

### [`agent_tool/`](agent_tool/)
- (See subfolder for details.)
- Demonstrates agent-to-agent tool integration within ADK agents.

### [`built-in/`](built-in/README.md)
- **Purpose:** Built-in tools for code execution, Google search, RAG, and VertexAI search.
- **Key Examples:**
  - [`code_execution/`](built-in/code_execution/README.md): Math/code execution agent.
  - [`google_search/`](built-in/google_search/README.md): Google search agent.
  - [`rag_engine/`](built-in/rag_engine/README.md): Vertex AI RAG corpus retrieval agent.
  - [`vertexai_search/`](built-in/vertexai_search/README.md): Vertex AI Search data store agent.
- **Limitation:** Only one built-in tool per agent; cannot be used in sub-agents.

### [`function/`](function/README.md)
- **Purpose:** Function tool integration for calling external APIs.
- **Key Examples:**
  - [`multiple_call/`](function/multiple_call/README.md): Multiple function tools (exchange rates, stock prices).
  - [`single_call/`](function/single_call/README.md): Single function tool (exchange rates).

### [`langchain/`](langchain/README.md)
- **Purpose:** LangChain-powered tools for advanced web search and data retrieval.
- **Key Example:**
  - [`tavily_search/`](langchain/tavily_search/README.md): Tavily web search and exchange rate agent.

### [`mcp/`](mcp/README.md)
- **Purpose:** Model Context Protocol (MCP) tools for file system and custom server integration.
- **Key Examples:**
  - [`client_file_browser/`](mcp/client_file_browser/README.md): File browser agent via MCP.
  - [`server_exchange_rate/`](mcp/server_exchange_rate/README.md): Exchange rate agent via custom MCP server.

---

## Getting Started

1. Choose a subfolder based on your tool integration needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described in each example.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.