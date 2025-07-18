# ADK Loop Workflow Agent Example

## 1. Example Overview
This folder demonstrates a loop-based workflow agent using the Agent Development Kit (ADK). The agent is designed to process user input in a loop, allowing for iterative refinement, repeated questioning, or multi-turn tasks. This example is useful for scenarios where the agent needs to repeatedly interact with the user or perform a sequence of steps until a condition is met.

## 2. Environment Setting
Create a `.env` file in the parent folder (`adk/04-workflow/`) with the following content (adjust values as needed):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

## 3. How to Run the Source Code
1. Install dependencies as specified in the `pyproject.toml` or `requirements.txt`.
2. Navigate to the `adk/04-workflow/` directory in your terminal.
3. Run the agent using the ADK runner or a provided script. For example:
   ```bash
   adk web
   ```
   or, if a runner script is provided:
   ```bash
   uv run -m loop.runner
   ```
4. Interact with the agent via the web interface or terminal prompt.

## 4. License Information
This project is licensed under the Apache License 2.0.
