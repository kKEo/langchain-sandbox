"""
Exercise 5: Handle Agent Failures Gracefully

TASK:
Create an agent with error handling that gracefully handles:
1. Tool failures
2. Max iteration limits
3. Invalid queries
4. Parsing errors

INSTRUCTIONS:
1. Create tools that can fail (with error conditions)
2. Build an agent with error handling parameters using AgentExecutor
3. Implement try-except blocks around agent_executor.invoke()
4. Provide meaningful error messages
5. Test various failure scenarios

HINT: Use max_iterations and handle_parsing_errors on AgentExecutor
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain import hub
# from langchain.agents import AgentExecutor, create_react_agent
# from langchain_core.tools import Tool
# from langchain_openai import ChatOpenAI

# TODO: Create a tool that can fail
# def unreliable_tool(query: str) -> str:
#     if "fail" in query.lower():
#         raise ValueError("Tool failure")
#     return "Success"

# TODO: Create tools list
# tools = [...]

# TODO: Initialize agent with error handling
# prompt = ...
# agent = ...
# agent_executor = AgentExecutor(
#     ...,
#     max_iterations=3,
#     handle_parsing_errors=True
# )

# TODO: Test with error scenarios
# test_cases = [
#     ("Normal query", "Should succeed"),
#     ("Query with fail", "Should handle error"),
#     ("Invalid format", "Should handle parsing error")
# ]

print("Exercise 5: Complete the code above to handle agent failures")

