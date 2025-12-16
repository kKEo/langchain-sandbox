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
2. Initialize agent with error handling parameters
3. Implement try-except blocks around agent.run()
4. Provide meaningful error messages
5. Test various failure scenarios

HINT: Use max_iterations, handle_parsing_errors parameters
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain...

# TODO: Create a tool that can fail
# def unreliable_tool(query: str) -> str:
#     if "fail" in query.lower():
#         raise ValueError("Tool failure")
#     return "Success"

# TODO: Create tools list
# tools = [...]

# TODO: Initialize agent with error handling
# agent = initialize_agent(
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

