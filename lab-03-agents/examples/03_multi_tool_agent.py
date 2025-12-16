"""
Example: Agent with Multiple Tools

This example demonstrates an agent that uses multiple tools
to answer complex queries.
"""
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool, WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def multi_tool_agent_example():
    """Demonstrate agent with multiple tools."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create multiple tools
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    
    def calculator(expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def text_length(text: str) -> str:
        """Get the length of a text string."""
        return str(len(text))
    
    def reverse_string(text: str) -> str:
        """Reverse a string."""
        return text[::-1]
    
    # Create tool objects
    tools = [
        WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for mathematical calculations. Input should be a valid Python expression."
        ),
        Tool(
            name="TextLength",
            func=text_length,
            description="Useful for getting the length of a text string. Input should be a string."
        ),
        Tool(
            name="ReverseString",
            func=reverse_string,
            description="Useful for reversing a string. Input should be a string."
        )
    ]
    
    # Initialize agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5
    )
    
    # Run the agent
    print("Running multi-tool agent...")
    print("=" * 70)
    
    queries = [
        "What is the capital of France and what is 25 * 4?",
        "Look up information about Python programming language, then calculate the length of the word 'Python'",
        "Reverse the string 'LangChain' and calculate 100 / 4"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 70)
        try:
            result = agent.run(query)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        print("-" * 70)

if __name__ == "__main__":
    multi_tool_agent_example()

