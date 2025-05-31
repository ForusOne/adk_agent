# adk/06-deploy/

This directory contains code and utilities for deploying, managing, and interacting with AI agents using Vertex AI Agent Engine. It provides scripts and modules for agent deployment, session management, updating agents, and integration with Google Cloud infrastructure.

## Subfolders

---

### agent_engine/

**Purpose:**  
Contains scripts and modules for building, deploying, and managing agent engines on Vertex AI.

**Key Files:**
- `agent.py`:  
  Defines how to build a root agent or a sequential agent pipeline, often composed of multiple sub-agents (e.g., `positive_critic`, `negative_critic`, `review_critic`).
- `agent_mgmt.py`:  
  Provides functions for deploying agents (`deploy_agent`), retrieving agent engines (`get_agent_engine`), listing all agents (`show_agents`), and deleting agents (`delete_agent`). These functions interact with Vertex AI's agent engine APIs and handle configuration such as display name, GCS directory, requirements, and extra packages.
- `deploy.py`:  
  Script for initializing and running an ADK application with a given agent and user query. Handles Vertex AI environment setup, agent deployment, and streaming of agent responses. Also demonstrates how to deploy and update agents on the remote engine.

**Features:**
- Full lifecycle management for agent engines (deploy, update, list, delete).
- Integration with Google Cloud Storage and Vertex AI.
- Command-line interface for deployment and management tasks.

---

### agent_session/

**Purpose:**  
Provides session management and agent invocation utilities for agents deployed on Vertex AI Agent Engine.

**Key Files:**
- `engine.py`:  
  Contains `create_agent_engine`, which initializes Vertex AI and creates a new agent engine instance with a display name and description.
- `session.py`:  
  Provides `call_agent` (sends a user query to the agent and prints the response) and `run_agent` (runs a conversational loop with the agent, managing sessions and user input). Uses `VertexAiSessionService` for session management.
- `update.py`:  
  Contains `update_remote_agent`, which updates an existing agent engine with new agent code, requirements, and description.

**Features:**
- Session creation and management for conversational agents.
- Support for updating deployed agents with new logic or dependencies.
- Command-line interface for running and updating agent sessions.

---

## General Features

- **Environment Integration:**  
  All scripts use environment variables (via `dotenv`) for configuration, such as project ID, location, and GCS bucket.
- **Google Cloud Integration:**  
  Uses Vertex AI's Python SDK for agent engine management, session handling, and deployment.
- **Command-Line Usability:**  
  Most scripts are designed to be run from the command line with arguments for agent names, user IDs, session IDs, and queries.
- **Extensibility:**  
  The modular design allows for easy extension with new agent types, tools, or deployment strategies.

---

## Example Use Cases

- Deploying a new agent pipeline to Vertex AI and making it available for user queries.
- Listing, updating, or deleting deployed agent engines.
- Running a conversational session with a deployed agent, maintaining session state.
- Updating an agent engine with new code or requirements without redeploying from scratch.

---

This structure enables robust, cloud-native deployment and management of AI agents, supporting both development and production workflows on Google Cloud Vertex AI.
