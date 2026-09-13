from agno.agent import Agent
from agno.models.groq import Groq
from agno.os import AgentOS
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    model=Groq(id="openai/gpt-oss-20b"),
    instructions="You are a helpful assistant.",
    markdown=True,
)

agent_os = AgentOS(
    agents=[agent],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agentos:app", reload=True)