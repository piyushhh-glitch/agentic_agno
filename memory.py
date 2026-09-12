from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

from dotenv import load_dotenv

load_dotenv()

db=SqliteDb(db_file="agno.db")


def build_agent():
    return Agent(
        name="Agent with memory",
        db=db,
        model=Groq(id="openai/gpt-oss-20b"),
        instructions="You are an helpful AI assistant.",
        markdown=True,
        add_history_to_context=True,
        update_memory_on_run=True
    )

memory_agent=build_agent()

user_id="piyush@gmail.com"

memory_agent.print_response(
    "My name is Piyush & I am a data scientist at Amazon .What is the capital of Australia?",
    user_id=user_id
    )
memory_agent.print_response(
    "who am i and where do i work?.What is the best time to visit it ?",
    user_id=user_id
    )

memories=memory_agent.get_user_memories(
    user_id=user_id
)

print("Memories:")
pprint(memories)