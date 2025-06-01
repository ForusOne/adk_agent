# ADK Agent Engine Deployment Example

This folder demonstrates how to build, manage, deploy, and run a multi-agent pipeline using the Agent Development Kit (ADK) and Vertex AI Agent Engine. It provides scripts and utilities for local testing, deployment to Vertex AI, and remote execution.

---

## Overview

This example shows how to:
- Build a multi-stage agent pipeline using `SequentialAgent`
- Define and register sub-agents for different review perspectives
- Deploy the agent pipeline to Vertex AI Agent Engine
- Manage agent engines (deploy, list, retrieve, delete)
- Run and test the agent both locally and remotely

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
adk/06-deploy/agent_engine/
├── __init__.py
├── agent.py
├── agent_mgmt.py
├── deploy.py
├── run.py
├── sub_agent.py
├── README.md
```

- `agent.py`  
  Defines the main pipeline agent as a `SequentialAgent` composed of multiple sub-agents (positive, negative, and review critics).
- `sub_agent.py`  
  Implements the sub-agents: `positive_critic`, `negative_critic`, and `review_critic`, each with its own instruction and behavior.
- `agent_mgmt.py`  
  Provides functions to deploy, retrieve, list, and delete agent engines on Vertex AI using the Vertex AI Python SDK.
- `deploy.py`  
  Script for local testing, deployment, and running the agent pipeline on Vertex AI. Handles environment setup, deployment, and streaming responses.
- `run.py`  
  Script for running a deployed agent engine remotely by resource name, streaming responses for a given user and session.
- `__init__.py`  
  Marks the folder as a Python package.



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

## Deployment & Management (`agent_mgmt.py`, `deploy.py`, `run.py`)

- **Deploying an Agent**: Use `deploy.py` to deploy the pipeline agent to Vertex AI. Handles requirements, GCS storage, and metadata.
- **Listing/Getting/Deleting Agents**: Use functions in `agent_mgmt.py` to manage agent engines on Vertex AI.
- **Running Locally**: `deploy.py` can also run the agent locally for unit testing.
- **Running Remotely**: Use `run.py` to send queries to a deployed agent engine by resource name.

---

## Example Usage

### 1. deploy command
```
ai_agent/adk/06-deploy$ uv run -m agent_engine.deploy --agent_name 'shins777' --user_id forus --query 'What is the Generative AI?'
```

### 2. run command
```
ai_agent/adk/06-deploy$ uv run -m agent_engine.run --resource_name projects/7217743942/locations/us-central1/reasoningEngines/11277477728768 --user_id forus --session_id 851727717299353600 --query 'What is the Generative AI?'
```
    * resource_name : resouce name of agent
    * user_id : user id.
    * session_id : it should be already existed in agent engine if you want to specify session_id.

---

## License

This project is licensed under the Apache License 2.0.
