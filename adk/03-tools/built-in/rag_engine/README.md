
## Note to execute the example.

1. Configuration.
    ```
    GOOGLE_GENAI_USE_VERTEXAI = TRUE
    GOOGLE_CLOUD_PROJECT = <Project ID> ex> "ai-forus"
    GOOGLE_CLOUD_LOCATION = <Location> ex> "us-central1"

    MODEL = <Model Name>  ex> "gemini-2.0-flash"

    RAG_CORPUS = <RAG_CORPUS> ex> "projects/ai-forus/locations/us-central1/ragCorpora/488021312309353728"

    ```

2. Install package
    llama_index
    ```
    uv add llama_index
    ```

3. Login to GCP
    ```
    gcloud auth list
    gcloud auth application-default login
    ```

4. run 
    ```
    adk web
    ```


    