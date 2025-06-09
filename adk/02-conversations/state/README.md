# State Conversation Example (ADK)

## Example Overview
This folder demonstrates how to use the ADK framework to build agents that manage stateful conversations, allowing for advanced context and flow control.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
Run the state conversation agent with:

```bash
uv run python agent.py
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../../LICENSE) file for details.
