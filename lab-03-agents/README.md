# Lab 3: Agents and Tools - Dynamic Decision Making

**Level: Intermediate**

## Learning Objectives

By the end of this lab, you will be able to:
- Understand the agent-executor pattern
- Create custom tools for agents
- Integrate external APIs and functions
- Build agents that can reason and use tools dynamically
- Handle agent errors and retries

## Prerequisites

- Completion of Labs 1 and 2
- Understanding of chains and memory
- Basic knowledge of APIs and function calls

## Setup

1. Install lab-specific dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Some exercises may require additional API keys (e.g., for web search)

## Topics Covered

1. **Agent Types**
   - Zero-shot ReAct agents
   - Plan-and-Execute agents
   - ReAct document agents

2. **Tool Creation**
   - Built-in tools (Wikipedia, Calculator, Search)
   - Custom tool development
   - Tool error handling

3. **Agent Executors**
   - Agent execution loops
   - Max iterations and timeouts
   - Error handling and retries

4. **Advanced Agent Patterns**
   - Multi-tool agents
   - Agent observability
   - Debugging agent behavior

## Exercises

1. **Exercise 1**: Create a research agent that searches and summarizes
2. **Exercise 2**: Build a calculator agent with custom math tools
3. **Exercise 3**: Implement a weather + news agent using multiple tools
4. **Exercise 4**: Create a custom tool for database queries
5. **Exercise 5**: Handle agent failures gracefully

## Examples

- `01_basic_agent.py` - Simple agent with built-in tools
- `02_custom_tool.py` - Creating custom tools
- `03_multi_tool_agent.py` - Agent with multiple tools
- `04_agent_error_handling.py` - Error handling patterns
- `05_agent_observability.py` - Debugging and monitoring

## Key Concepts

### Basic Agent

```python
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool

tools = [Tool(name="Search", func=search_func, description="...")]
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

### Custom Tool

```python
from langchain_core.tools import BaseTool

class CustomTool(BaseTool):
    name = "custom_tool"
    description = "Tool description"
    
    def _run(self, query: str) -> str:
        # Tool logic
        return result
```

## Next Steps

After completing this lab, proceed to [Lab 4: RAG Systems](../lab-04-rag/README.md).

