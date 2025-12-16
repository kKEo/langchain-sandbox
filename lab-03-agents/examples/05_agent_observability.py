"""
Example: Agent Observability and Debugging

This example demonstrates how to observe and debug agent behavior
using verbose mode and custom callbacks.
"""
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.callbacks import StdOutCallbackHandler
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

class AgentCallback(StdOutCallbackHandler):
    """Custom callback for agent observability."""
    
    def on_agent_action(self, action, **kwargs):
        """Called when agent takes an action."""
        print(f"\n[AGENT ACTION] Tool: {action.tool}, Input: {action.tool_input}")
    
    def on_tool_end(self, output, **kwargs):
        """Called when tool execution ends."""
        print(f"[TOOL OUTPUT] {output}")
    
    def on_agent_finish(self, finish, **kwargs):
        """Called when agent finishes."""
        print(f"[AGENT FINISH] {finish.return_values}")

def observability_example():
    """Demonstrate agent observability."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create tools
    def calculator(expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for mathematical calculations."
        )
    ]
    
    # Initialize agent with verbose mode and callbacks
    callbacks = [AgentCallback()]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,  # Enable verbose output
        callbacks=callbacks  # Add custom callbacks
    )
    
    # Run the agent
    print("Running agent with observability...")
    print("=" * 70)
    
    query = "What is 15 * 23 + 100? Then multiply the result by 2."
    print(f"Query: {query}")
    print("=" * 70)
    
    result = agent_executor.invoke({"input": query}, callbacks=callbacks)
    
    print("\n" + "=" * 70)
    print(f"Final Result: {result['output']}")
    print("=" * 70)

if __name__ == "__main__":
    observability_example()

