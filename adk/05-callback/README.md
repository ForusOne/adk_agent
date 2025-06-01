# ADK Callback Examples

This directory contains advanced examples of using callbacks in the Agent Development Kit (ADK) to control agent, model, and tool behavior. Each subfolder demonstrates a different callback mechanism, allowing you to intercept, modify, or block execution at various stages of the agent workflow.

---

## Subfolders & Summaries

### [`agent_callback/`](agent_callback/README.md)
Demonstrates agent-level callbacks for pre- and post-processing around the main agent logic. You can:
- Skip agent execution or override responses based on session state
- Implement custom, state-driven conversational flows
- Respond in a structured format or handle casual conversation naturally

---

### [`model_callback/`](model_callback/README.md)
Demonstrates model-level (LLM) callbacks for pre- and post-processing around the LLM call. You can:
- Block LLM calls based on keywords in user input
- Block or modify responses based on keywords in the LLM output
- Implement content moderation and custom flows

---

### [`tool_callback/`](tool_callback/README.md)
Demonstrates tool-level callbacks for pre- and post-processing around tool execution. You can:
- Modify tool arguments before execution (e.g., normalize country names)
- Modify tool results after execution (e.g., add notes to results)
- Implement custom, context-driven tool flows

---

## License

This project is licensed under the Apache License 2.0.
