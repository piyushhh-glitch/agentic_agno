# The agent uses Yahoo Finance to turn a plain-English question into tool calls and a current market brief.

from agno.agent import Agent
from agno.models.google import GeminiInteractions
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def agent_with_tools():
    return  Agent(name="Agent-with-tools",
                model=GeminiInteractions(id="gemini-3.6-flash"),
                instructions=[
                "Use Yahoo Finance for facts that can change.",
                "Lead with the answer, then show the evidence.",
                "Use a table when comparing companies.",
                "Say when data is unavailable; never invent a value.",
                "Keep the response concise and do not give personalized financial advice."
                ],
                tools=[YFinanceTools(
                    enable_company_info=True,
                    enable_stock_fundamentals=True,
                    enable_company_news=True
                )],
                markdown=True,
                add_datetime_to_context=True)


gemini_agent=agent_with_tools()

gemini_agent.print_response("Give me a quick market brief on Nvdia",stream=True)

    
