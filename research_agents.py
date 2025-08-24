from dotenv import load_dotenv
from agents import Agent, function_tool
from tavily import TavilyClient
import difflib
load_dotenv()
tavily_client = TavilyClient()

@function_tool
def check_source(result: str) -> str:
    """
    Enhanced source checking:
    Returns result with reliability + type of source.
    """
    if ".gov" in result or ".edu" in result:
        reliability = "High"
        source_type = "Official / Academic"
    elif "wikipedia" in result or "industry" in result:
        reliability = "Medium"
        source_type = "General Reference"
    else:
        reliability = "Low"
        source_type = "Unverified / Misc"

    return f"{result}\n[Source Reliability: {reliability}, Source Type: {source_type}]"

@function_tool
def detect_conflict(text_a: str, text_b: str) -> str:
    """
    Simple conflict detector:
    Compares two research outputs and flags contradictions.
    """
    similarity = difflib.SequenceMatcher(None, text_a, text_b).ratio()
    if similarity < 0.3:  # threshold for contradiction
        return f"⚠️ Potential Conflict Detected between sources:\n- {text_a[:150]}...\n- {text_b[:150]}..."
    else:
        return "✅ No major conflict detected (sources agree or are complementary)."


@function_tool
def search(query: str) -> str:
    try:
        response = tavily_client.search(query)
        return response
    except Exception as e:
        return f"Search failed: {str(e)}"

fact_finder_agent = Agent(
    name="FactFinder",
    instructions=(
        "You are a dedicated fact-finding research specialist. "
        "Your job is to search widely across trusted sources and gather accurate, up-to-date, "
        "and well-supported information. "
        "Always focus on factual correctness, avoid speculation, "
        "and provide clear summaries of your findings."
    ),
    tools=[search]
)

source_checker_agent = Agent(
    name="SourceChecker",
    instructions=(
        "You are a source evaluation expert. "
        "Your job is to carefully examine each research result and assign a reliability rating "
        "(High, Medium, Low) along with identifying the source type "
        "(e.g., Official/Academic, General Reference, Unverified). "
        "Always highlight why a source is credible or questionable. "
        "Ensure the reliability note is added clearly to the text."
    ),
    tools=[check_source]
)


conflict_detector_agent = Agent(
    name="ConflictDetector",
    instructions=(
        "You are a conflict analysis specialist. "
        "Your job is to compare research findings from different agents and determine "
        "whether they agree, complement each other, or contradict each other. "
        "If contradictions are detected, flag them clearly with ⚠️ and provide a short summary "
        "of the conflicting claims. "
        "If no contradiction is found, state explicitly that the sources are consistent ✅."
    ),
    tools=[detect_conflict]
)


research_agents = [
    fact_finder_agent,
    source_checker_agent,
    conflict_detector_agent
]