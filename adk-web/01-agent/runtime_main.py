import asyncio
import argparse
from dotenv import load_dotenv
from runtime import runner

load_dotenv()

def main() -> None:
    """Parses command line arguments and runs the basic agent."""

    print("Running the agent...")

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