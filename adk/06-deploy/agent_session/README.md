# ADK Agent Session Deployment Example

This folder demonstrates how to build, manage, deploy, update, and run a multi-agent pipeline with session management using the Agent Development Kit (ADK) and Vertex AI Agent Engine. It provides scripts and utilities for local and remote execution, session handling, and agent engine management.

---

## Overview

This example shows how to:
- Build a multi-stage agent pipeline using `SequentialAgent`
- Define and register sub-agents for different review perspectives
- Deploy and update the agent pipeline to Vertex AI Agent Engine
- Manage agent engines (deploy, list, retrieve, delete)
- Run and test the agent with session management

---

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"

STAGING_BUCKET="gs://ai-agent-0417"

```
---

## Login to GCP
To deploy an agent, need to login to GCP and Vertex AI.
   * GCP Login
    ```
    gcloud auth application-default login 
    ```
   * Vertex AI 
    ```
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )    
    ```

---

## Folder Structure

```
adk/06-deploy/agent_session/
├── agent.py
├── agent_mgmt.py
├── engine.py
├── session.py
├── sub_agent.py
├── update.py
├── README.md
```

- `agent.py`  
  Defines the main pipeline agent as a `SequentialAgent` composed of multiple sub-agents (positive, negative, and review critics).
- `sub_agent.py`  
  Implements the sub-agents: `positive_critic`, `negative_critic`, and `review_critic`, each with its own instruction and behavior.
- `agent_mgmt.py`  
  Provides functions to deploy, retrieve, list, and delete agent engines on Vertex AI using the Vertex AI Python SDK.
- `engine.py`  
  Script for creating and deploying an agent engine on Vertex AI.
- `session.py`  
  Script for running the agent in a conversational loop with session management, using Vertex AI sessions.
- `update.py`  
  Script for updating a deployed agent engine with the latest agent configuration.


---

## Agent Pipeline Details

- **`SequentialAgent`** (in `agent.py`):
  - Executes a sequence of sub-agents: `positive_critic`, `negative_critic`, and `review_critic`.
  - Each sub-agent provides a different perspective or summary on the user's query.
- **Sub-agents** (in `sub_agent.py`):
  - `positive_critic`: Writes a positive review on a topic.
  - `negative_critic`: Writes a negative review on a topic.
  - `review_critic`: Summarizes and concludes based on the previous reviews.

---

## Session Management & Deployment

- **Deploying an Agent**: Use `agent_mgmt.py` or `engine.py` to deploy the pipeline agent to Vertex AI. Handles requirements, GCS storage, and metadata.
- **Updating an Agent**: Use `update.py` to update a deployed agent engine with the latest code and configuration.
- **Running with Sessions**: Use `session.py` to run the agent in a conversational loop, maintaining session state for each user.

---

## Example Usage

### 1. Agent Engine creation

```
uv run -m agent_session.engine --agent_name forusone
```

### 2. session test.
You can create a session and see the session in Agent Engine of Vertex AI in GCP Console. 
If you use same session id, you cna see the session information was persisted.
```
uv run -m agent_session.session --agent_engine_id 112774703328768 --user_id forus --session_id 8517270633353600
```

### 3. update Agent Engine.
```
uv run -m agent_session.update --agent_engine_id 497173105427968
```

---

## License

This project is licensed under the Apache License 2.0.
