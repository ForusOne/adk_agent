### Note for execute

0. Configuration.
    ```
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=<Google Gemini API Key>
                    
    PROJECT_ID = <GCP Project ID>
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
    ```
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )    
    ```

2. deploy and run agent

    1. deploy command
    ```
    uv run -m agent_engine.deploy --agent_name 'shins777' --user_id forus --query 'What is the Generative AI?'
    ```
    2. run command
    ```
    uv run -m agent_engine.run --resource_name projects/721521243942/locations/us-central1/reasoningEngines/112774708637728768 --user_id forus --session_id 8517270617299353600 --query 'What is the Generative AI?'
    ```
    * resource_name : resouce name of agent
    * user_id : user id.
    * session_id : it should be already existed in agent engine if you want to specify session_id.
   

