# ADK Workflow Agents Overview

This directory contains advanced workflow agent examples using the Agent Development Kit (ADK). Each subfolder demonstrates a different approach to orchestrating multi-step, modular, and iterative agent workflows, including custom, general, loop, parallel, and sequential patterns.

---

## Subfolders Overview

### 1. `custom/` — Custom Critique Workflow Agent
- Orchestrates a multi-step critique workflow using custom logic and sub-agents for positive, negative, and review critiques.
- Supports conditional, stepwise evaluation and review of user input or generated content.
- See [`custom/README.md`](./custom/README.md) for details.

### 2. `general/` — General Workflow Agent
- Answers user questions by delegating critique tasks to sub-agents for positive and negative reviews.
- Organizes the intent of the user's question before providing a response.
- See [`general/README.md`](./general/README.md) for details.

### 3. `loop/` — Loop Workflow Agent
- Uses a combination of sequential and loop agents to research, critique, refine, and summarize answers.
- Supports iterative improvement and review, with early exit if the answer is satisfactory.
- See [`loop/README.md`](./loop/README.md) for details.

### 4. `parallel/` — Parallel Workflow Agent
- Runs positive and negative critique sub-agents in parallel, then summarizes the results with a review agent in a sequential pipeline.
- Demonstrates modular agent design using ADK's parallel and sequential agent architecture.
- See [`parallel/README.md`](./parallel/README.md) for details.

### 5. `sequencial/` — Sequential Workflow Agent
- Runs positive and negative critique sub-agents in sequence, then summarizes the results with a review agent.
- Enables a structured workflow for critique and review.
- See [`sequencial/README.md`](./sequencial/README.md) for details.

---


## Getting Started

1. Choose a subfolder (`custom`, `general`, `loop`, `parallel`, or `sequencial`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.
