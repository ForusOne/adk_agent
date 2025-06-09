# Google Search Tool Example (ADK)

## Example Overview
This folder demonstrates how to use the built-in Google Search tool with ADK agents to answer user queries using real-time web search results.

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
Run the Google Search agent with:

```bash
uv run python agent.py
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../../../LICENSE) file for details.
