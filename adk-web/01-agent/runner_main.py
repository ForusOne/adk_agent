import asyncio
import argparse
import os

from cmd import runner

# Constants
PROJECT_ID = "ai-hangsik"
LOCATION = "us-central1"

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = PROJECT_ID
os.environ["GOOGLE_CLOUD_LOCATION"] = LOCATION

def main() -> None:
    """Parses command line arguments and runs the basic agent."""
    parser = argparse.ArgumentParser(description="Run the basic ADK agent with a user query.")
    parser.add_argument(
        "query",
        type=str,
        help="The query/message to send to the agent.",
    )
    args = parser.parse_args()
    asyncio.run(runner.run_basic_agent(user_query=args.query))

if __name__ == "__main__":
    main()