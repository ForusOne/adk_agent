# AI Agent on ADK(Agent Development Kit)

The source codes in this repository were developed using VS Code, but it's IDE-agnostic.  
Note : https://code.visualstudio.com/

## Install uv package manager.
### 1. uv install
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or 
```
pip install uv
```

## 2. uv init

Initialize venv with **pyproject.toml** file which should be located in **the same directory**.  
You have to have **pyproject.toml** in the **/adk_agent/adk** directory.

```
/adk_agent/adk$ uv venv --python 3.12
```

Activate the virtual environment
```
/adk_agent/adk$ source .venv/bin/activate
(adk) adk_agent/adk$
```

Deactivate the virtual environment
```
/adk_agent/adk$ deactivate
```

###  3. command examples
```
uv init
uv add ruff==2.2.2
uv --help
```

###  4. Unit test

Create .env file in **adk_agent/adk/01-agent/***
```
(adk) /adk_agent/adk/01-agent$ ls -al
total 16
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 .
drwxr-xr-x  18 forus  pgroup   576 Jun  2 08:21 ..
-rw-r--r--   1 forus  pgroup   198 Jun  2 08:26 .env
-rw-r--r--   1 forus  pgroup  3178 Jun  2 08:20 README.md
drwxr-xr-x   6 forus  pgroup   192 Jun  2 08:25 basic
drwxr-xr-x   8 forus  pgroup   256 Jun  2 08:20 runtime
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 search
(adk) /adk_agent/adk/01-agent$
```

Sample .env file 

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzaSyD6ugbCWYZVM2uZh6Bd8

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "721523942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

Run the unit test
```
(adk) /adk_agent/adk/01-agent$ adk web
```

Type in the chat : What is Generative AI ?