### Ollama 

1. install ollama
   ```
   uv add ollama
   ```
2. ollama command.
   ```
   ollama show
   ollama list
   ollama pull gemma3
   ollama run gemma3
   ollama stop gemma3
   ```
3. Run local test with ollama python library.
   ```
   uv run ollama_test.py
   ```
4. Before run agent, set the env.
   ```
   export OLLAMA_API_BASE="http://localhost:11434"
   adk web
   ```