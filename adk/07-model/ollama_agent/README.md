# ADK Ollama Agent Example

This folder demonstrates how to build and use an LLM agent powered by Ollama models (such as Llama 3 and Gemma) within the Agent Development Kit (ADK) framework. It includes code for agent construction, model selection, and direct Ollama API testing.

---

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"

OLLAMA_API_BASE="http://localhost:11434"

```

---

## Folder Structure

```
adk/07-model/ollama_agent/
├── __init__.py
├── agent.py
├── ollama_test.py
├── README.md
```

- `agent.py`  
  Defines the main LLM agent using the Ollama backend (Llama 3 or Gemma), with a structured instruction template and model selection logic.
- `ollama_test.py`  
  Simple script to test direct interaction with an Ollama server using the `ollama` Python client.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Overview

This example shows how to:
- Build an LLM agent using Ollama models (Llama 3 or Gemma) via the ADK `LlmAgent` and `LiteLlm` wrappers
- Select the model dynamically by name
- Provide clear, structured answers to user questions
- Test direct API calls to a local Ollama server

---

## Agent Details (`agent.py`)

- Uses `LlmAgent` from `google.adk.agents` and `LiteLlm` from `google.adk.models.lite_llm`
- Supports model selection: `llama` (Llama 3) or `gemma` (Gemma 3)
- Instruction template enforces structured answers:
  - Question content
  - Question intent
  - Answer content
- Answers casual questions naturally and always in the user's language
- Example instantiation: `root_agent = build_agent("gemma")`

---

## Ollama API Test (`ollama_test.py`)
```
ai_agent/adk/07-model$ uv run ollama_test.py
```

---
## Example Usage

Note : Execute the following command on **07-model** folder. 
```
ai_agent/adk/07-model$ export OLLAMA_API_BASE="http://localhost:11434"
ai_agent/adk/07-model$ adk web
```

---

## License

This project is licensed under the Apache License 2.0.
