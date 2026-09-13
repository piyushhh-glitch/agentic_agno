from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool(requires_confirmation=True)
def send_email(to: str, subject: str, message: str) -> str:
    """Send email to recipient.

    Args:
        to: Email address of the recipient.
        subject: Email subject.
        message: Email body.
    """
    return f"Email sent to {to} with subject: {subject}"


agent = Agent(
    name="Email Assistant",
    model=Groq(id="openai/gpt-oss-20b"),
    tools=[send_email],
    instructions=[
        "You are an email assistant.",
        "Use the send_email tool when the user asks you to send an email.",
    ],
    markdown=True,
)


agent.print_response(
    "Send an email to john@example.com saying that the meeting is scheduled for tomorrow.",
    stream=True,
)