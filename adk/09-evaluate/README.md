
1. ADK Eval
    https://google.github.io/adk-docs/evaluate/#3-adk-eval-run-evaluations-via-the-cli

    Command : 
    ```
    adk eval agent_eval \
        agent_eval/data/conversation.test.json \
        --config_file_path=agent_eval/data/test_config.json \
        --print_detailed_results
    ```
    Issue reported.
    https://github.com/google/adk-samples/issues/96

2. pytest
    https://google.github.io/adk-docs/evaluate/#2-pytest-run-tests-programmatically

    : Need to install several pytest-*** packages before using pytest
    : Dose not look work now --> async issues. 

    Command :
    ```
    uv run pytest -m agent_eval
    ```