"""
Example: Creating Custom Tools

This example demonstrates how to create custom tools by
inheriting from BaseTool.
"""
import os
from dotenv import load_dotenv
from typing import Optional
from langchain.tools import BaseTool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from pydantic import Field

# Load environment variables
load_dotenv()

class WeatherTool(BaseTool):
    """Tool for getting weather information (simulated)."""
    name = "weather"
    description = "Useful for getting current weather information for a city. Input should be a city name."
    
    def _run(self, city: str) -> str:
        """Get weather for a city (simulated)."""
        # In a real scenario, this would call a weather API
        weather_data = {
            "New York": "Sunny, 72°F",
            "London": "Cloudy, 15°C",
            "Tokyo": "Rainy, 22°C",
            "Paris": "Partly cloudy, 18°C"
        }
        return weather_data.get(city, f"Weather data not available for {city}")
    
    async def _arun(self, city: str) -> str:
        """Async version (not implemented)."""
        raise NotImplementedError("Async not implemented")

class TimeTool(BaseTool):
    """Tool for getting current time in a timezone (simulated)."""
    name = "time"
    description = "Useful for getting the current time in a timezone. Input should be a timezone name like 'EST' or 'PST'."
    
    def _run(self, timezone: str) -> str:
        """Get time in timezone (simulated)."""
        import datetime
        time_data = {
            "EST": datetime.datetime.now().strftime("%H:%M:%S EST"),
            "PST": datetime.datetime.now().strftime("%H:%M:%S PST"),
            "UTC": datetime.datetime.utcnow().strftime("%H:%M:%S UTC")
        }
        return time_data.get(timezone.upper(), f"Timezone {timezone} not found")
    
    async def _arun(self, timezone: str) -> str:
        """Async version (not implemented)."""
        raise NotImplementedError("Async not implemented")

def custom_tool_example():
    """Demonstrate custom tool usage."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create custom tools
    tools = [WeatherTool(), TimeTool()]
    
    # Initialize agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    # Run the agent
    print("Running agent with custom tools...")
    print("=" * 70)
    
    queries = [
        "What's the weather in New York?",
        "What time is it in EST?",
        "What's the weather in Tokyo and what time is it in UTC?"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        print("-" * 70)
        result = agent.run(query)
        print(f"Result: {result}")
        print("-" * 70)

if __name__ == "__main__":
    custom_tool_example()

