# ADK Deployment Examples

This directory contains advanced examples for deploying, managing, and running multi-agent pipelines using the Agent Development Kit (ADK) and Vertex AI Agent Engine. Each subfolder demonstrates a different deployment and session management scenario, with scripts for local and remote execution, GCP integration, and agent engine management.

---

## Subfolders & Summaries

### [`agent_engine/`](agent_engine/README.md)
Demonstrates how to build, manage, deploy, and run a multi-agent pipeline using a `SequentialAgent` and Vertex AI Agent Engine. Includes scripts for:
- Local testing and deployment
- Registering and managing agent engines on Vertex AI
- Running deployed agents remotely

**Key Features:**
- Multi-stage agent pipeline (positive, negative, and review critics)
- GCP and Vertex AI integration
- Example `.env` and GCP login instructions

See [agent_engine/README.md](agent_engine/README.md) for details on folder structure, deployment, and usage.

---

### [`agent_session/`](agent_session/README.md)
Demonstrates how to build, manage, deploy, update, and run a multi-agent pipeline with session management. Includes scripts for:
- Creating and deploying agent engines
- Updating deployed agent engines
- Running agents in conversational loops with session state
- Managing agent engines on Vertex AI

**Key Features:**
- Session-aware agent pipeline
- Multi-stage review agents
- GCP and Vertex AI integration
- Example `.env` and GCP login instructions

See [agent_session/README.md](agent_session/README.md) for details on folder structure, session management, deployment, and usage.

---

## License

This project is licensed under the Apache License 2.0.
