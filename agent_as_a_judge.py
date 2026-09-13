from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.eval.agent_as_judge import AgentAsJudgeEval
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

# Stores evaluation-run results in a local SQLite database file.
db = SqliteDb(db_file="tmp/agent_as_judge_basic.db")

# The agent that generates an answer to evaluate.
agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    instructions=(
        "You are a technical writer. "
        "Explain concepts clearly and concisely."
    ),
    db=db,
)

# Run the agent and retain its response.
response = agent.run("Explain what an API is")

# A separate Groq-backed LLM evaluates the agent's answer.
evaluation = AgentAsJudgeEval(
    name="Explanation Quality",
    model=Groq(id="openai/gpt-oss-120b"),
    criteria=(
        "Explanation should be clear, beginner-friendly, "
        "and use simple language"
    ),
    scoring_strategy="numeric",  # Score from 1 to 10
    threshold=7,                 # Pass when score >= 7
    db=db,
)

# Give the evaluator the original question and the agent's generated answer.
result = evaluation.run(
    input="Explain what an API is",
    output=str(response.content),
    print_results=True,
)