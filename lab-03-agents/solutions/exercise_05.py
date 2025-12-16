"""
Solution to Exercise 5: Handle Agent Failures Gracefully
"""
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Create a tool that can fail
def unreliable_tool(query: str) -> str:
    """A tool that fails under certain conditions."""
    if "fail" in query.lower() or "error" in query.lower():
        raise ValueError("Simulated tool failure: Tool cannot process this query")
    if "timeout" in query.lower():
        raise TimeoutError("Simulated timeout error")
    return f"Successfully processed: {query}"

def normal_tool(query: str) -> str:
    """A normal tool that always succeeds."""
    return f"Result for '{query}': Operation completed successfully"

# Create tools list
tools = [
    Tool(
        name="UnreliableTool",
        func=unreliable_tool,
        description="A tool that processes queries but may fail. Use with caution."
    ),
    Tool(
        name="NormalTool",
        func=normal_tool,
        description="A reliable tool that always succeeds."
    )
]

# Initialize agent with error handling
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,  # Limit iterations to prevent infinite loops
    handle_parsing_errors=True  # Handle parsing errors gracefully
)

# Test with error scenarios
test_cases = [
    ("Process this normal query", "Should succeed"),
    ("Process this query with fail", "Should handle tool error gracefully"),
    ("Process timeout query", "Should handle timeout error"),
]

print("Testing Agent Error Handling")
print("=" * 70)

for query, expected in test_cases:
    print(f"\nTest Case: {expected}")
    print(f"Query: {query}")
    print("-" * 70)
    
    try:
        result = agent_executor.invoke({"input": query})
        print(f"✓ Success: {result['output']}")
    except ValueError as e:
        print(f"✗ Caught ValueError: {e}")
        print("  Agent handled tool failure gracefully")
    except TimeoutError as e:
        print(f"✗ Caught TimeoutError: {e}")
        print("  Agent handled timeout gracefully")
    except Exception as e:
        print(f"✗ Caught {type(e).__name__}: {e}")
        print("  Agent handled error gracefully")
    print("-" * 70)

# Test max iterations
print("\n" + "=" * 70)
print("Testing Max Iterations Limit")
print("=" * 70)

def recursive_tool(query: str) -> str:
    """A tool that always suggests another action."""
    return "You should ask me again with a different query to continue."

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
    result = limited_agent.invoke({"input": "Process this query"})
    print(f"Result: {result['output']}")
except Exception as e:
    print(f"Agent stopped due to max iterations: {type(e).__name__}")
    print("This is expected behavior to prevent infinite loops.")

