# Deep Research Agent System

This is a multi-agent research system inspired by OpenAI Deep Research.  
It uses **streaming output** so that you can see live updates while agents are working.

---

## 📌 Features

- **Planning Agent (with streaming):** Breaks down a complex query into smaller steps, streams the research plan as it is built.
- **Fact Finder Agent (with streaming):** Searches for facts in real-time and streams partial findings.
- **Source Checker Agent (with streaming):** Validates sources step by step and streams confidence levels.
- **Conflict Detector Agent (with streaming):** Detects contradictions between findings and streams conflict alerts live.
- **Final Report Generator (with streaming):** Synthesizes all results into a professional report, streaming it as sections are completed.

---


## System Flow
User Query
│
▼
Planning Agent ──> Research Tasks
│
▼
Research Agents (parallel)
│
▼
Conflict Detection & Synthesis Agent
│
▼
Report Writer Agent ──> Final Report (streamed + traced)


---

## Agents & Roles

| Agent | Role |
|-------|------|
| **Planning Agent** | Breaks questions into smaller, actionable tasks |
| **Research Agents** | Gather information from multiple sources concurrently |
| **Synthesis Agent** | Combines results, resolves conflicts, organizes insights |
| **Report Writer Agent** | Produces the final report and manages live output |
| **Lead Researcher** | Oversees the workflow, assigns tasks, and tracks progress |

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenAI Agents SDK
- AsyncIO for concurrency
- Streaming API for live updates

---

## Environment Variables (.env):

SEARCH_API_KEY=<your_search_api_key>
OPENAI_API_KEY=<your_openai_api_key>
TAVILY_API_KEY=<optional_if_using_tavily>

---


## Setup & Requirements

1. **Python 3.10+**  
2. **UV environment:** `pip install uv`  
3. **Dependencies:**  

```bash
pip install asyncio python-dotenv openai
```

---


### Running the System
```bash
python deep_research_system.py
```
- The console shows each agent’s progress (tracing).
- The final report streams directly in real time.


## Advanced Features

- Conflict Resolution: Contradictions are flagged during synthesis
- Creative Strategies: Agents dynamically adapt their approach to the query
- Error Handling: Prevents crashes during API calls or agent failures
- Tracing: View live progress for each agent
- Dynamic Instructions: Automatically recognizes keywords like summarize or deeper
- Optional enhancements:
    - Source quality assessment (High/Medium/Low)
    - Automatic citation management [1], [2], [3]
    - User profile personalization


### Project Structure
```
deep_research_system/
│
├── deep_research_system.py       # LeadResearcher agent & main orchestrator
├── research_agents.py            # Specialist research agents
├── planning_agent.py             # Planning agent for breaking down questions
├── synthesis_agent.py            # Synthesis agent to combine insights
├── report_writer.py              # Generates final report with streaming
├── .env                          # Environment variables (API keys)
├── README.md                     # Project documentation
└── requirements.txt              # Optional pip dependencies

```