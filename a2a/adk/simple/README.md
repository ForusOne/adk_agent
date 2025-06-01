
1. install package  
    uv add python-a2a : https://pypi.org/project/python-a2a  
    uv add a2a-sdk : https://pypi.org/project/a2a-sdk  

2. start server  
    ```
    uv run -m simple.server 
    ```
3. start client  
    ```
    uv run -m simple.client
    ```
4. check agent card.  

    ```
    curl http://0.0.0.0:7777/.well-known/agent.json
    ```
