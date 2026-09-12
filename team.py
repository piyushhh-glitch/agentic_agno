from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent=Agent(name="English Agent",role="You answer questions in English.")
chi_agent=Agent(name="Chinese Agent",role="You answer questions in Chinese.")
mar_agent=Agent(name="Marathi Agent",role="You answer questions in Marathi.")
hin_agent=Agent(name="Hindi Agent",role="You answer questions in Hindi.")

team=Team(
    name="Answer and translation Team",
    members=[eng_agent,chi_agent,hin_agent,mar_agent],
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True,
    show_members_responses=True,
    instructions=""" All member agents must respond to answer the query in their specific language. 
                        Do not route to just one agent.
                        Output the response of all agents.
                """
)



team.print_response("What is the capital of India?")