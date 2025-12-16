"""
Example: Basic Agent with Built-in Tools

This example demonstrates how to create a simple agent using
built-in tools like Wikipedia and Calculator.
"""
import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def basic_agent_example():
    """Demonstrate basic agent usage."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create tools
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    
    # Define a simple calculator tool
    def calculator(expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    calc_tool = Tool(
        name="Calculator",
        func=calculator,
        description="Useful for performing mathematical calculations. Input should be a valid Python expression."
    )
    
    # Get the react prompt template
    prompt = hub.pull("hwchase17/react")
    
    # Create agent with tools
    tools = [wikipedia, calc_tool]
    agent = create_react_agent(llm, tools, prompt)
    
    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )
    
    # Run the agent
    print("Running agent...")
    print("=" * 70)
    
    queries = [
        "What is the population of Tokyo?",
        "What is 15 * 23 + 100?",
        "Who wrote '1984' and what is 2^8?"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 70)
        result = agent_executor.invoke({"input": query})
        print(f"Result: {result['output']}")
        print("-" * 70)

if __name__ == "__main__":
    basic_agent_example()

