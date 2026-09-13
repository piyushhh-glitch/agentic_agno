# 🤖 Agentic AI with Agno

A repository for learning and building Agentic AI applications using the Agno framework.

## 📖 Content

- Introduction to Agentic AI
- Agno Framework
- AI Agents
- Models & LLMs
- Tools & Function Calling
- Agent Instructions
- Workflows
- State & Context
- Memory
- Multi-Agent Systems
- MCP
- Guardrails
- Human-in-the-Loop
- Evaluation & Observability

## 📂 Files

### `agent.py`
A basic Agno agent using the DuckDuckGo tool for web search.  
Demonstrates agent creation, tools, instructions, and context.

### `finance.py`
A Finance Agent using YFinance and DuckDuckGo tools.  
Demonstrates how an agent can use multiple tools to retrieve stock prices, financial data, and analyst recommendations.

### `youtube_video_analyzer.py`
A YouTube video analysis agent using the YouTube tool.  
Analyzes videos by generating an overview, timestamps, topic segments, key learning points, and important references.

### `team.py`
A multi-agent team containing English, Hindi, Marathi, and Chinese agents.  
Demonstrates how multiple agents can work together and return responses in different languages.

### `memory.py`
An Agno agent with persistent memory using SQLite.  
Demonstrates storing user-specific memories, adding conversation history to context, and retrieving saved memories across interactions.

### `ui.py`
A Streamlit web interface for the YouTube Video Analyzer.  
Demonstrates how to connect an Agno agent to a simple UI where users can enter a YouTube link and receive an AI-generated analysis report.

### `workflow.py`
A content creation workflow using multiple Agno agents.  
Demonstrates how agents can be organized into sequential steps, where a researcher gathers information and a writer uses it to create an article.

### `pii_detection.py`
Demonstrates PII detection guardrails for protecting sensitive user information.  
Shows how to block requests containing PII and how to mask detected PII instead of blocking the request.

### `prompt_injection.py`
Demonstrates protection against prompt injection attacks using Agno's Prompt Injection Guardrail.  
Tests how the agent handles requests that attempt to override its instructions or bypass restrictions.

### `human_in_the_loop.py`
Demonstrates Human-in-the-Loop using tool confirmation.  
The agent requires human approval before executing an action, such as sending an email.