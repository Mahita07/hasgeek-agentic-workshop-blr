# Multi-Agent Workflow — Exam Helper

A clean, minimal multi-agentic system built with **LangGraph** and **Google Gemini**.

---

## Architecture

```
User Message
     │
     ▼
┌─────────────────────────────────────────────────┐
│           Orchestrator Agent (ReAct)            │
│                                                 │
│   ┌──────────────┐   ┌──────────────────────┐  │
│   │   explainer  │   │       learner         │  │
│   │    (tool)    │   │       (tool)          │  │
│   └──────────────┘   └──────────────────────┘  │
└─────────────────────────────────────────────────┘
     │
     ▼
Final Response
```

**One LangGraph node. Two agents as tools. Zero extra complexity.**

| File | Role |
|------|------|
| `multi_agentic_workflow.py` | LangGraph graph definition (`START → orchestrator → END`) |
| `agents/orchestrator_agent.py` | Orchestrator with ReAct loop, holds explainer & learner as tools |
| `agents/explainer_agent.py` | Explains concepts simply (beginner-friendly) |
| `agents/learner_agent.py` | Provides exam-ready structured study material |
| `main.py` | Interactive CLI entry point |

---

## Setup

**1. Install dependencies**
```bash
uv sync
# or
pip install -e .
```

**2. Set your API key**
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

**3. Run**
```bash
python main.py
```

Or run a single query:
```bash
python main.py "Explain recursion simply"
```

---

## Running Notion MCP Server

To use the Notion MCP integration, follow these steps:

**1. Get your Notion token**

Obtain your Notion API token from [Notion Integrations](https://www.notion.so/profile/integrations/internal).

**2. Run the Notion MCP server (Terminal 1)**

In one terminal, start the Notion MCP server:
```bash
NOTION_TOKEN="your_notion_token" npx @notionhq/notion-mcp-server \
  --transport http \
  --port 3000 \
  --auth-token "mysecret123"
```
Replace `your_notion_token` with your actual Notion token. You can use any auth token of your choice (e.g., `"mysecret123"`).

**3. Configure environment variables**

In your `.env` file, ensure all values are set and the auth token matches the one used when starting the server:
```bash
MCP_AUTH_TOKEN=mysecret123  # Must match the --auth-token used above
```

Inside notion application, create a page and in its connections, add the connection to the notion mcp server.
Add the parent page id in the .env file.
```bash
PARENT_PAGE_ID=your_parent_page_id
```
**4. Run the application (Terminal 2)**

In another terminal, run the application:
```bash
python main.py
```

---

## How it works

1. User sends a message.
2. The **OrchestratorAgent** (a LangGraph ReAct agent) reads the message and decides which tool to call:
   - **`explainer`** — simple explanation, analogies, beginner-friendly
   - **`learner`** — in-depth, exam-ready structured notes
3. The chosen tool runs the corresponding agent and returns the response.
4. The workflow stores conversation history for multi-turn context.

