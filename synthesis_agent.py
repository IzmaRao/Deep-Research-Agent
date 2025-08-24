from dotenv import load_dotenv
from agents import Agent, ModelSettings
load_dotenv()

synthesis_agent = Agent(
    name="SynthesisAgent",
    instructions=(
        "You are an expert synthesizer of research findings. "
        "Your task is to combine outputs from multiple research agents into a single, "
        "coherent, and well-structured report. Ensure consistency, logical flow, "
        "and clarity. Reorganize content if needed, remove redundancies, and maintain "
        "professional tone suitable for formal reports. Highlight key insights clearly."
    ),
    model="gpt-4o-mini",
    model_settings=ModelSettings(
        temperature=0.3,         
        max_output_tokens=700,
    )
)


