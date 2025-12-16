"""
Solution to Exercise 1: Create a Research Agent
"""
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create Wikipedia tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Initialize agent
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, [wikipedia], prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=[wikipedia],
    verbose=True
)

# Run research query
query = "What is machine learning and its main applications?"
print(f"Research Query: {query}")
print("=" * 70)

result = agent_executor.invoke({"input": query})

print("\n" + "=" * 70)
print("Research Result:")
print(result["output"])
print("=" * 70)

