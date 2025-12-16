"""
Solution to Exercise 2: Build a Calculator Agent with Custom Math Tools
"""
import os
from dotenv import load_dotenv
import math
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define math functions
def add(expression: str) -> str:
    """Add two numbers. Input format: 'a + b'"""
    try:
        parts = expression.split('+')
        result = sum(float(p.strip()) for p in parts)
        return str(result)
    except:
        return "Error in addition"

def multiply(expression: str) -> str:
    """Multiply numbers. Input format: 'a * b'"""
    try:
        parts = expression.split('*')
        result = 1
        for p in parts:
            result *= float(p.strip())
        return str(result)
    except:
        return "Error in multiplication"

def power(expression: str) -> str:
    """Calculate power. Input format: 'base ^ exp' or 'base ** exp'"""
    try:
        if '^' in expression:
            base, exp = expression.split('^')
        elif '**' in expression:
            base, exp = expression.split('**')
        else:
            return "Use ^ or ** for power"
        result = float(base.strip()) ** float(exp.strip())
        return str(result)
    except:
        return "Error in power calculation"

def sqrt_calc(number: str) -> str:
    """Calculate square root. Input: a number"""
    try:
        result = math.sqrt(float(number.strip()))
        return str(result)
    except:
        return "Error in square root"

# Create Tool objects
tools = [
    Tool(
        name="Add",
        func=add,
        description="Adds numbers. Input format: 'a + b'"
    ),
    Tool(
        name="Multiply",
        func=multiply,
        description="Multiplies numbers. Input format: 'a * b'"
    ),
    Tool(
        name="Power",
        func=power,
        description="Calculates power. Input format: 'base ^ exp'"
    ),
    Tool(
        name="SquareRoot",
        func=sqrt_calc,
        description="Calculates square root. Input: a number"
    )
]

# Initialize agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Test with queries
queries = [
    "What is 15 + 23?",
    "Calculate 5 to the power of 3",
    "What is the square root of 144 multiplied by 2?"
]

for query in queries:
    print(f"\nQuery: {query}")
    print("-" * 70)
    result = agent.run(query)
    print(f"Result: {result}")
    print("-" * 70)

