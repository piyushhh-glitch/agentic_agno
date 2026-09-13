from agno.agent import Agent
from agno.guardrails import PIIDetectionGuardrail
from agno.models.groq import Groq  
from agno.run import RunStatus

from dotenv import load_dotenv
load_dotenv()


def check_input(agent: Agent, label: str, text: str, expect_blocked: bool) -> None:
    response = agent.run(input=text)

    # PII-blocked runs return RunStatus.error
    blocked = response.status == RunStatus.error

    print(f"{label}: {'blocked' if blocked else 'allowed'}")
    if response.content:
        print(response.content)

    # Confirms each test result matches the expected outcome
    assert blocked == expect_blocked


def main():
    agent = Agent(
        name="Privacy-Protected Agent",
        model=Groq(id="openai/gpt-oss-120b"),  # Changed
        pre_hooks=[PIIDetectionGuardrail()],
        description="An agent that helps with customer service while protecting privacy.",
        instructions=(
            "You are a helpful customer service assistant. "
            "Always protect user privacy and handle sensitive information appropriately."
        ),
    )

    cases = [
        ("Normal request", "Can you help me understand your return policy?", False),
        ("SSN", "My Social Security Number is 123-45-6789.", True),
        ("Credit card", "My card number is 4532 1234 5678 9012.", True),
        ("Email", "Send the receipt to john.doe@example.com.", True),
        ("Phone", "My phone number is 555-123-4567.", True),
        (
            "Multiple PII types",
            "My email is john@company.com and phone is 555.987.6543.",
            True,
        ),
        ("Unseparated credit card", "My card is 4532123456789012.", True),
    ]

    for label, text, expect_blocked in cases:
        check_input(agent, label, text, expect_blocked)

    # This version masks detected PII rather than blocking the request.
    masked_agent = Agent(
        name="Privacy-Protected Agent (Masked)",
        model=Groq(id="openai/gpt-oss-120b"),  # Changed
        pre_hooks=[PIIDetectionGuardrail(mask_pii=True)],
        description="An agent that helps with customer service while protecting privacy.",
        instructions=(
            "You are a helpful customer service assistant. "
            "Always protect user privacy and handle sensitive information appropriately."
        ),
    )

    masked_agent.print_response(
        input=(
            "Hi, my Social Security Number is 123-45-6789. "
            "Can you help me with my account?"
        ),
    )


if __name__ == "__main__":
    main()