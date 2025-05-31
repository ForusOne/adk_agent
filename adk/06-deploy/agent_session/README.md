### Note to execute

This source code was written on information from the following manual.   
https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/sessions/manage-sessions-adk

0. Configuration.
    ```
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=<Google Gemini API Key>
                    
    PROJECT_ID = <GCP Project ID>
    PROJECT_NUMBER = <GCP Project Number>
    LOCATION = <Locatioin> ex> "us-central1"
    MODEL = <Model Name>  ex> "gemini-2.0-flash"

    STAGING_BUCKET="gs://agent-0417"
    ```

1. Create a bucket to store agent artifacts files while deploying.
    Set the information in .env
    ```
    STAGING_BUCKET="gs://agent-0417"
    ```

2. To deploy an agent, need to login to GCP and Vertex AI.
   * GCP Login
    ```
    gcloud auth application-default login 
    ```
   * Vertex AI 
    The following code should be to create or update Agent engine in Vertex AI.
    ```
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )    
    ```

3. engine create and deploy

    1. Agent Engine creation
    ```
    uv run -m agent_session.engine --agent_name forusone
    ```

    2. session test.
    You can create a session and see the session in Agent Engine of Vertex AI in GCP Console. 
    If you use same session id, you cna see the session information was persisted.
    ```
    uv run -m agent_session.session --agent_engine_id 112774708637728768 --user_id forus --session_id 8517270617299353600
    ```
    
    3. update Agent Engine.
    ```
    uv run -m agent_session.update --agent_engine_id 4971736494105427968
    ```

