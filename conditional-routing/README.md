# Conditional Routing Agent

An example agentic workflow demonstrating conditional routing in Langgraph. It asks the user how they are feeling, utilizes a Gemini-2.5-flash LLM model to assess whether the user's energy level is "low", "medium", or "high", and routes the workflow to one of three corresponding handler nodes to provide activity suggestions.

## Setup

1. Make sure you have `uv` installed.
2. Clone this repository and navigate to this directory.
3. Copy `.env.example` to `.env` and fill in your `GOOGLE_API_KEY`.
   ```bash
   cp .env.example .env
   ```
4. Run the application:
   ```bash
   uv run app.py
   ```
