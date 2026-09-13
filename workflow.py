from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.hackernews import HackerNewsTools
from agno.workflow import Workflow

from dotenv import load_dotenv
load_dotenv()

researcher=Agent(
    name="Researcher",
    instructions="Find relevant information about the topic",
    model=Groq(id="openai/gpt-oss-20b"),
    tools=[HackerNewsTools()]
)

writter=Agent(
    name="Writter",
    instructions="Write a clear, engaging article based on the research",
    model=Groq(id="openai/gpt-oss-20b")
)

content_workflow=Workflow(
    name="content creation",
    steps=[researcher,writter]
)

content_workflow.print_response("Write an article about AI Trends",stream=True)