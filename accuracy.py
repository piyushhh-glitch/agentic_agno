from typing import Optional

from agno.agent import Agent
from agno.tools.calculator import CalculatorTools
from agno.models.groq import Groq
from agno.eval.accuracy import AccuracyEval , AccuracyResult

from dotenv import load_dotenv
load_dotenv()

evaluation=AccuracyEval(
    name="Calculator Evaluation",
    model=Groq(id="openai/gpt-oss-20b"),
    agent=Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[CalculatorTools()]
    ),
    input="What is 10*5 then to the power of 2? do it step by step",
    expected_output="2500",
    additional_guidelines="Agent output should include the steps and the final answer.",
    num_iterations=3,
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8