from agno.agent import Agent
from agno.models.google import GeminiInteractions
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are an helpful and expert Travel agent",
        add_datetime_to_context=True,

    )

gemini_agent=build_agent()

gemini_agent.print_response("Is it safe to go UAE today?")