
## Note to execute the example.

1. Configuration.
    ```
    GOOGLE_GENAI_USE_VERTEXAI=TRUE
    GOOGLE_CLOUD_PROJECT = <GCP Project ID> ex > "ai-forus"
    GOOGLE_CLOUD_LOCATION = <Locatioin> ex> "global"
    PROJECT_NUMBER = <GCP Project Number > ex> "7215222243942"

    MODEL = <Model Name>  ex> "gemini-2.0-flash"

    DATASTORE_ID = <DATASTORE_ID> ex> "it-laws-ds_1713063479348"

    ```

2. Login to GCP
    ```
    gcloud auth list
    gcloud auth application-default login
    ```

3. run
    ```
    adk web
    
    or 
    
    uv run -m vertexai_search.runner --query "What is the Google's 2023 revenue ?"
    ```

4. Something to know. 

    if you have the following error 
        ```
        ValueError: retrieval parameter is not supported in Gemini API.
        ```
        you have to set the env. 
        ```
        GOOGLE_GENAI_USE_VERTEXAI = TRUE
        ```
