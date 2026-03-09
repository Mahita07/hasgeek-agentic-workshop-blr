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

## How it works

1. User sends a message.
2. The **OrchestratorAgent** (a LangGraph ReAct agent) reads the message and decides which tool to call:
   - **`explainer`** — simple explanation, analogies, beginner-friendly
   - **`learner`** — in-depth, exam-ready structured notes
3. The chosen tool runs the corresponding agent and returns the response.
4. The workflow stores conversation history for multi-turn context.

