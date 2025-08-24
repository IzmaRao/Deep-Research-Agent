from dotenv import load_dotenv
from agents import Agent, ModelSettings
from pydantic import BaseModel
load_dotenv()

class ReportOutput(BaseModel):
    title: str
    summary: str
    citations: list[str]

report_writer_agent = Agent(
    name="ReportWriter",
    instructions="""
    You are a professional research report writer.
    Take all findings and write a clear, well-structured report in human-readable format.
    Use headings, subheadings, bullet points, and numbered citations like [1], [2].
    Do NOT return JSON. Just output a normal report as plain text.
    """,
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0.7,
        max_output_tokens=1000,
        json_schema=ReportOutput.model_json_schema()
    ),
)
