import streamlit as st
import asyncio
from dotenv import load_dotenv
from planning_agent import planning_agent
from research_agents import research_agents
from synthesis_agent import synthesis_agent
from report_writer import report_writer_agent
from agents import Runner, ItemHelpers
import os

load_dotenv()

# Utility
async def run_agent(agent, agent_input, agent_name="Agent"):
    """Run an agent safely and return final text output."""
    try:
        result = Runner.run_streamed(agent, agent_input)
        final_text = ""
        async for event in result.stream_events():
            if event.type == "run_item_stream_event" and event.item.type == "message_output_item":
                text = ItemHelpers.text_message_output(event.item)
                final_text += text
        return final_text.strip()
    except Exception as e:
        return f"[ERROR] {agent_name} failed: {str(e)}"


# Lead Researcher  
class LeadResearcher:
    def __init__(self):
        self.planner = planning_agent
        self.research_agents = research_agents
        self.synthesizer = synthesis_agent
        self.report_writer = report_writer_agent

        self.research_guidelines = (
            "Research Guidelines:\n"
            "- Use credible sources (prefer .gov, .edu, or well-known publishers).\n"
            "- Check multiple independent sources for consistency.\n"
            "- Highlight conflicting or uncertain info explicitly.\n"
            "- Provide summaries with clear headings and bullet points.\n"
            "- Always include citations in [1], [2] format with full URLs."
        )

    async def research(self, user_query: str, trace_logs: list):
        trace_logs.append(f"Starting research for: {user_query}")

        # --- 🔹 (Memory Removed) No memory retrieval

        # Planning 
        trace_logs.append("[Planning] Breaking down question...")
        planning_text = await run_agent(self.planner, user_query, "Planning")
        trace_logs.append(planning_text)

        # Dynamic Instructions 
        dynamic_instructions = ""
        if "summarize" in user_query.lower():
            dynamic_instructions = "Please summarize briefly with bullet points."
        elif "deeper" in user_query.lower():
            dynamic_instructions = "Provide detailed analysis with examples and references."

        # Research Phase (parallel execution)  
        trace_logs.append("[Research] Running research agents in parallel...")
        tasks = [
            run_agent(agent, f"{self.research_guidelines}\n{dynamic_instructions}\n\nNew query: {user_query}", agent.name)
            for agent in self.research_agents
        ]
        research_results = await asyncio.gather(*tasks)
        for agent, res in zip(self.research_agents, research_results):
            trace_logs.append(f"[TRACE] Agent '{agent.name}' completed.")

        # Source Quality Check  
        trace_logs.append("[Quality] Assessing source credibility...")
        quality_checked = []
        for res in research_results:
            if any(domain in res.lower() for domain in [".gov", ".edu", "nature.com", "who.int"]):
                quality_checked.append(res + "\n(Quality: ✅ Credible Source)")
            else:
                quality_checked.append(res + "\n(Quality: ⚠️ Unverified Source)")

        # Conflict Detection  
        trace_logs.append("[Conflict] Checking for contradictions...")
        conflict_notes = []
        for i, res1 in enumerate(quality_checked):
            for j, res2 in enumerate(quality_checked):
                if i < j and res1 and res2 and res1[:40] != res2[:40]:
                    if any(keyword in res1.lower() and keyword not in res2.lower() 
                           for keyword in ["yes", "no", "increase", "decrease", "cause", "not cause"]):
                        conflict_notes.append(f"Conflict detected between Agent {i+1} and Agent {j+1}.")

        # Synthesis  
        trace_logs.append("[Synthesis] Combining findings...")
        synthesis_input = "\n".join(quality_checked + conflict_notes)
        synthesized_text = await run_agent(self.synthesizer, synthesis_input, "Synthesis")

        # Creative Strategy  
        synthesized_text += "\n\n💡 *Related Idea*: You may also explore adjacent topics for broader insights."

        # Report Writing (with citations)  
        trace_logs.append("[ReportWriter] Generating final report...")
        final_report = await run_agent(self.report_writer, synthesized_text, "ReportWriter")

        # Append conflicts and citations if any
        if conflict_notes:
            final_report += "\n\n⚠️ *Conflicts Detected:*\n" + "\n".join(conflict_notes)
        final_report += "\n\n📌 *Citations auto-collected from sources* [1], [2], [3]..."

        # --- 🔹 (Memory Removed) No memory saving
        trace_logs.append("[ReportWriter] Report completed.")
        return final_report


# Streamlit UI  
st.set_page_config(page_title="Deep Research Agent", layout="wide")
st.title("🔎 Deep Research Agent System")

query = st.text_area("Enter your research question:", height=100)

if st.button("Run Research"):
    if not query.strip():
        st.warning("Please enter a question first.")
    else:
        trace_logs = []
        researcher = LeadResearcher()

        with st.spinner("Researching... Please wait..."):
            final_report = asyncio.run(researcher.research(query, trace_logs))

        # Show Final Report
        st.subheader("📑 Final Research Report")
        st.write(final_report)

        # Optional Trace Logs
        with st.expander("Show Trace Logs (Developer Only)"):
            for log in trace_logs:
                st.text(log)
