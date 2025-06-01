# ADK Built-in Tools Overview

## Subfolders Overview

### 1. `code_execution/` — Built-in Code Execution Agent
- Solves mathematical expressions by writing and executing Python code.
- Returns both the code and the result as plain text.
- See [`code_execution/README.md`](./code_execution/README.md) for details.

### 2. `google_search/` — Built-in Google Search Agent
- Answers user queries by performing a Google search and formatting responses with source information.
- See [`google_search/README.md`](./google_search/README.md) for details.

### 3. `rag_engine/` — Built-in RAG Engine Agent
- Retrieves relevant documentation and reference materials from a Vertex AI RAG corpus.
- Returns answers with citations.
- See [`rag_engine/README.md`](./rag_engine/README.md) for details.

### 4. `vertexai_search/` — Built-in Vertex AI Search Agent
- Answers user queries by searching a specified Vertex AI Search data store.
- Returns structured answers with source information.
- See [`vertexai_search/README.md`](./vertexai_search/README.md) for details.

---

## Getting Started

1. Choose a subfolder (`code_execution`, `google_search`, `rag_engine`, or `vertexai_search`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

## Limitation as of June 2025:

* Currently, for each root agent or single agent, only one built-in tool is supported. No other tools of any type can be used in the same agent.
* Built-in tools cannot be used within a sub-agent.


For more information, see the individual README files in each subfolder.
