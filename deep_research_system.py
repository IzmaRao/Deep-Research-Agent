from agents import Runner, ItemHelpers
from planning_agent import planning_agent
from research_agents import research_agents
from synthesis_agent import synthesis_agent
from report_writer import report_writer_agent
import asyncio
from dotenv import load_dotenv

load_dotenv()


class LeadResearcher:
    def __init__(self):
        # Initialize all agents
        self.planner = planning_agent
        self.research_agents = research_agents
        self.synthesizer = synthesis_agent
        self.report_writer = report_writer_agent

        # Guidelines for research agents
        self.research_guidelines = (
            "Research Guidelines:\n"
            "- Use credible sources (.gov, .edu).\n"
            "- Check facts from multiple sources.\n"
            "- Highlight conflicting info if found.\n"
            "- Summarize clearly with headings and bullet points.\n"
            "- Include citations in [1], [2] format with full URLs."
        )

    async def stream_agent_run(self, agent, agent_input, agent_name=None):
        """
        Stream outputs from any agent in real-time.
        Shows message outputs and tool outputs.
        """
        result = Runner.run_streamed(agent, agent_input)
        final_text = ""

        async for event in result.stream_events():
            # Ignore raw token events
            if event.type == "raw_response_event":
                continue

            # Print message outputs
            elif event.type == "run_item_stream_event":
                if event.item.type == "message_output_item":
                    text = ItemHelpers.text_message_output(event.item)
                    if agent_name:
                        print(f"[{agent_name}] {text}", end="", flush=True)
                    else:
                        print(text, end="", flush=True)
                    final_text += text

                # Print outputs of any tools used by agents
                elif event.item.type == "tool_call_output_item":
                    print(f"[{agent_name} Tool Output]: {event.item.output}")

        return final_text

    async def research(self, user_query: str):
        print("\n[LeadResearcher] Starting research for:", user_query)

        # --- Planning Phase ---
        print("\n[Planning] Breaking down your question...")
        planning_text = await self.stream_agent_run(self.planner, user_query, "Planning")
        print("\n[Planning] Tasks generated:\n", planning_text)

        # --- Set instructions dynamically based on query ---
        dynamic_instructions = ""
        if "summarize" in user_query.lower():
            dynamic_instructions = "Please summarize the information in short bullet points."
        elif "deeper" in user_query.lower():
            dynamic_instructions = "Provide detailed analysis with examples."

        # --- Research Phase ---
        print("\n[Research] Running research agents in parallel...")
        research_tasks = [
            self.stream_agent_run(
                agent,
                f"{self.research_guidelines}\n{dynamic_instructions}\n{user_query}",
                agent.name
            )
            for agent in self.research_agents
        ]
        research_results = await asyncio.gather(*research_tasks)

        # Log agent completion
        for agent, result_text in zip(self.research_agents, research_results):
            print(f"\n[TRACE] Agent '{agent.name}' finished research.\n{'-'*50}")

        # --- Synthesis Phase ---
        print("\n[Synthesis] Combining all research findings...")
        synthesis_input = "\n".join(research_results)
        synthesized_text = await self.stream_agent_run(self.synthesizer, synthesis_input, "Synthesis")

        # --- Report Writing Phase ---
        print("\n[ReportWriter] Generating final report...\n")
        final_report = await self.stream_agent_run(self.report_writer, synthesized_text, "ReportWriter")

        print("\n[ReportWriter] Report completed.\n")
        return final_report


async def main():
    lead_researcher = LeadResearcher()
    query = input("Enter your research question: ")
    final_report = await lead_researcher.research(query)

    print("\n\n===== FINAL REPORT =====\n")
    print(final_report)


if __name__ == "__main__":
    asyncio.run(main())
