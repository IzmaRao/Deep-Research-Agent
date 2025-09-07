from dotenv import load_dotenv
from agents import Agent, input_guardrail, GuardrailFunctionOutput, RunContextWrapper, ModelSettings, TResponseInputItem
load_dotenv()

@input_guardrail
async def research_only_guard(
    ctx: RunContextWrapper,
    agent: Agent,
    user_input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    text = user_input if isinstance(user_input, str) else " ".join(item.content for item in user_input)
    allowed = any(word in text.lower() for word in ["research", "study", "analysis", "science", "history", "technology", "health"])
    return GuardrailFunctionOutput(is_allowed=allowed, reason="Not research-related." if not allowed else None)


planning_agent = Agent(
    name="PlanningAgent",
    instructions=(
        "You are a highly skilled research planner. "
        "Your task is to break down a complex research question into a clear, structured plan. "
        "Divide the report into logical sections such as Introduction, Key Findings, Analysis, "
        "and Conclusion. Suggest headings, subheadings, and bullet points where appropriate. "
        "Ensure the flow is easy to follow and covers all important aspects of the topic. "
        "Focus on clarity, organization, and completeness of the research outline."
    ),
    model="gpt-4o-mini",  
    input_guardrails=[research_only_guard],
    model_settings=ModelSettings(
        temperature=0.5,          
        max_output_tokens=500,  
        top_p=0.9,              
    )
)
