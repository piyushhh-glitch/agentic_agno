from agno.agent import Agent
from agno.eval.performance import PerformanceEval
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

def run_agent():
    agent = Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        system_message="Be concise, reply with one sentence.",
    )

    response=agent.run("What is the capital of France?")

    print(f"response :{response}")

    return response

simple_resp_performace=PerformanceEval(
    name="Simple performance evaluation",
    func=run_agent,
    num_iterations=1,
    warmup_runs=0
)

if __name__=="__main__":
    simple_resp_performace.run(print_results=True,print_summary=True)