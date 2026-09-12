# Finance Agent With DuckDuckGo and Yfinance 

from agno.agent import Agent
from agno.models.google import GeminiInteractions
from agno.models.groq import Groq

from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()


def build_agent():
    return Agent(
        name="Finance Agent",
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[YFinanceTools(),DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use tools whenever possible.",
                    "Use YFinanceTools for stock prices and financial data.",
                    "Use DuckDuckGoTools for web searches and analyst recommendations.",
                    "When using DuckDuckGoTools, always provide a search query.",
                    "Never pass a URL to the web_search tool.",
                    "Format your response using markdown.",
                    "Use tables to display data where possible."]
        # debug_mode=True
    )

finance_agent=build_agent()

finance_agent.print_response("Share the NVDA stock price and analyst recommendation?")
