from dotenv import load_dotenv
from agents import Agent, ModelSettings
load_dotenv()


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
    model_settings=ModelSettings(
        temperature=0.5,          
        max_output_tokens=500,  
        top_p=0.9,              
    )
)
