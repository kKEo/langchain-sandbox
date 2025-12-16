"""
Example: Agent Error Handling

This example demonstrates how to handle errors in agent execution,
including timeouts, max iterations, and tool errors.
"""
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def error_handling_example():
    """Demonstrate error handling in agents."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create a tool that might fail
    def unreliable_tool(query: str) -> str:
        """A tool that sometimes fails."""
        if "error" in query.lower():
            raise ValueError("Simulated tool error")
        return f"Successfully processed: {query}"
    
    tools = [
        Tool(
            name="UnreliableTool",
            func=unreliable_tool,
            description="A tool that processes queries but may fail. Use with caution."
        )
    ]
    
    # Initialize agent with error handling
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=3,  # Limit iterations to prevent infinite loops
        handle_parsing_errors=True  # Handle parsing errors gracefully
    )
    
    # Test scenarios
    print("Testing agent error handling...")
    print("=" * 70)
    
    test_cases = [
        ("Process this query", "Should succeed"),
        ("Process error query", "Should handle tool error"),
    ]
    
    for query, expected in test_cases:
        print(f"\nTest: {expected}")
        print(f"Query: {query}")
        print("-" * 70)
        try:
            result = agent_executor.invoke({"input": query})
            print(f"Result: {result['output']}")
        except Exception as e:
            print(f"Caught error: {type(e).__name__}: {e}")
        print("-" * 70)
    
    # Demonstrate max iterations
    print("\n" + "=" * 70)
    print("Testing max iterations limit...")
    print("=" * 70)
    
    # Create a tool that always returns a follow-up question
    def recursive_tool(query: str) -> str:
        """A tool that always suggests another action."""
        return "You should ask me again with a different query."
    
    recursive_tools = [
        Tool(
            name="RecursiveTool",
            func=recursive_tool,
            description="A tool that processes queries."
        )
    ]
    
    recursive_agent = create_react_agent(llm, recursive_tools, prompt)
    limited_agent = AgentExecutor(
        agent=recursive_agent,
        tools=recursive_tools,
        verbose=True,
        max_iterations=2  # Very low limit for demonstration
    )
    
    try:
        result = limited_agent.invoke({"input": "Process this"})
        print(f"Result: {result['output']}")
    except Exception as e:
        print(f"Agent stopped due to: {type(e).__name__}: {e}")

if __name__ == "__main__":
    error_handling_example()

