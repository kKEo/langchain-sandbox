"""
Solution to Exercise 1: Create a Research Agent
"""
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create Wikipedia tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Initialize agent
agent = initialize_agent(
    tools=[wikipedia],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run research query
query = "What is machine learning and its main applications?"
print(f"Research Query: {query}")
print("=" * 70)

result = agent.run(query)

print("\n" + "=" * 70)
print("Research Result:")
print(result)
print("=" * 70)

