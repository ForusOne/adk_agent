# ADK Function Tool Agents Overview

This directory contains examples of ADK (Agent Development Kit) agents that use function tools to answer user queries by calling external APIs. Each subfolder demonstrates a different approach to integrating and using function tools for real-world data retrieval.

---

## Subfolders Overview

### 1. `multiple_call/` — Multiple Function Tool Agent
- Answers user queries about exchange rates and stock prices by calling two different function tools.
- Uses the Frankfurter API for exchange rates and the Alphavantage API for stock prices.
- See [`multiple_call/README.md`](./multiple_call/README.md) for details.

### 2. `single_call/` — Single Function Tool Agent
- Answers user queries about exchange rates by calling a single function tool.
- Uses the Frankfurter API for exchange rates.
- See [`single_call/README.md`](./single_call/README.md) for details.

---

## Getting Started

1. Choose a subfolder (`multiple_call` or `single_call`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.
