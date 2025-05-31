
1. configuration
    ```
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=AIzaSyD6uPZRFklKVhvgp53gbCWYZVM2uZh6Bd8

    PROJECT_ID = "ai-hangsik"
    PROJECT_NUMBER = "721521243942"
    LOCATION = "us-central1"
    MODEL = "gemini-2.0-flash"
    ```

2. check npx, adk
    ```    
    which npx
    which adk
    ```

    if there is no npx, install the node js.
    download file https://nodejs.org/en and install node-v22.16.0.pkg

3. if there is some errors, upgrade the adk. as of June 1, the latest version is 1.1.1.
    ```
    uv add google-adk=1.1.1
    ```

4. run agent
    ```
    adk web
    ```
    
    command : List up file in client_file_browser
