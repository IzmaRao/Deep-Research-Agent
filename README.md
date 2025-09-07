<<<<<<< HEAD
# 🌐 Deep Research Agent System  

An intelligent multi-agent research framework inspired by **OpenAI Deep Research**.  
This system breaks down complex questions, runs parallel research across multiple agents, validates sources, detects conflicts, and finally generates a **streamed, traceable research report** in real time.  

---

## 🚀 What Makes It Special?  

- **Live Streaming Output** → Watch results appear as agents work.  
- **Parallel Agents** → Multiple research tasks run at the same time.  
- **Conflict Resolution** → Contradictions are detected and resolved.  
- **Source Validation** → Sources are checked step by step for reliability.  
- **Professional Reports** → A structured final report is generated with proper tracing.  

---

## 🎥 Demo  
👉 [Watch Agent Demo]([https://drive.google.com/file/d/1mvE7W4CfNhve4jPXB7lDIh7Ww5oQ8ub_/view?usp=sharing](https://drive.google.com/file/d/12jzLNak3JGiTenWmH0S7xFc-1pXtJRQO/view?usp=sharing))  

---

## 🔄 How It Works (System Flow)  

1. **User Query**  
   ⬇  
2. **Planning Agent** → Breaks the query into smaller research tasks  
   ⬇  
3. **Research Agents** → Work in parallel to collect facts  
   ⬇  
4. **Conflict Detection & Synthesis** → Finds contradictions and merges insights  
   ⬇  
5. **Report Writer Agent** → Streams the final polished report  

---

## 🧑‍🤝‍🧑 Agents & Their Roles  

| Agent | Responsibility |
|-------|----------------|
| **Planning Agent** | Splits complex queries into actionable research steps |
| **Research Agents** | Collect information from multiple sources concurrently |
| **Synthesis Agent** | Merges findings, resolves conflicts, organizes insights |
| **Report Writer Agent** | Produces the final structured report (with streaming) |
| **Lead Researcher** | Oversees workflow, assigns tasks, and tracks progress |

---

## ⚙️ Tech Stack  

- **Language:** Python 3.10+  
- **Framework:** OpenAI Agents SDK  
- **Concurrency:** AsyncIO  
- **Streaming:** Real-time API updates  

---

## 🔑 Environment Variables (.env)  

```
SEARCH_API_KEY=<your_search_api_key>
OPENAI_API_KEY=<your_openai_api_key>
TAVILY_API_KEY=<optional_if_using_tavily>
=======

# 🔎 Deep Research Agent System

This project is a **multi-agent research assistant** built with Streamlit and OpenAI’s Agent SDK.  
It plans research tasks, gathers information from multiple agents, synthesizes findings, and generates a structured report.

---

## 🚀 Features
- **Planning Agent** → Breaks down complex queries into smaller tasks.
- **Research Agents** → Run in parallel to gather information from diverse sources.
- **Synthesis Agent** → Combines results, highlights conflicts, and provides structured insights.
- **Report Writer** → Generates a polished report with citations.
- **Quality Checks** → Flags credible (.gov, .edu, WHO, etc.) vs. unverified sources.
- **Conflict Detection** → Identifies contradictory results between agents.
- **Streamlit UI** → User-friendly interface with trace logs for developers.

---

## 📂 Project Structure
```
deep_research_agent/
│── planning_agent.py
│── research_agents.py
│── synthesis_agent.py
│── report_writer.py
│── agents.py
│── deep_research_system.py   # Main Streamlit app
│── README.md
```

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/deep_research_agent.git
   cd deep_research_agent
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run deep_research_system.py
>>>>>>> ee2c019 (Updated README, agents, and config files)
```

Enter your research query in the text box and press **Run Research**.  
You’ll get a structured **Final Research Report** along with optional **trace logs**.

---

<<<<<<< HEAD
## 🛠️ Setup & Requirements  

1. Install **Python 3.10+**  
2. Install **UV environment:**  
   ```bash
   pip install uv
   ```  
3. Install dependencies:  
   ```bash
   pip install asyncio python-dotenv openai
   ```  

---

## ▶️ Running the System  

```bash
python deep_research_system.py
```  
=======
## 📌 Example Queries
- *"What are the health impacts of microplastics?"*
- *"Compare renewable energy adoption in the US vs Europe."*
- *"Summarize the effects of AI in education with credible sources."*

---

## ⚠️ Notes
- This version **does not use persistent memory (Mem0)**.  
- Each session starts fresh, with no stored context from past runs.

---

## 📜 License
MIT License – free to use and modify.
>>>>>>> ee2c019 (Updated README, agents, and config files)

- The console shows each agent’s live progress (tracing).  
- The final report is streamed directly in real time.  

<<<<<<< HEAD
---

## 🌟 Advanced Features  
=======
>>>>>>> ee2c019 (Updated README, agents, and config files)

- **Conflict Resolution:** Contradictions flagged during synthesis  
- **Creative Strategies:** Agents adapt dynamically to queries  
- **Error Handling:** Prevents crashes during API calls or failures  
- **Tracing:** View detailed progress for each agent  
- **Dynamic Instructions:** Understands keywords like *summarize* or *deeper*  
- **Optional Enhancements:**  
  - Source quality scoring (High/Medium/Low)  
  - Automatic citation management [1], [2], [3]  
  - Personalized user profiles  

---

## 📂 Project Structure  

<<<<<<< HEAD
```
deep_research_system/
│
├── deep_research_system.py       # LeadResearcher agent & orchestrator
├── research_agents.py            # Specialist research agents
├── planning_agent.py             # Planning agent for breaking down questions
├── synthesis_agent.py            # Combines insights & resolves conflicts
├── report_writer.py              # Generates final report with streaming
├── .env                          # Environment variables (API keys)
├── README.md                     # Project documentation
└── requirements.txt              # Optional pip dependencies
```
=======


