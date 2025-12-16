"""
Solution to Exercise 3: Weather + News Agent
"""
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

class WeatherTool(BaseTool):
    """Tool for getting weather information."""
    name = "weather"
    description = "Useful for getting current weather information for a city. Input should be a city name."
    
    def _run(self, city: str) -> str:
        """Get weather for a city (simulated)."""
        weather_data = {
            "New York": "Sunny, 72°F, Light breeze",
            "London": "Cloudy, 15°C, Drizzle expected",
            "Tokyo": "Rainy, 22°C, High humidity",
            "Paris": "Partly cloudy, 18°C, Pleasant",
            "San Francisco": "Foggy, 16°C, Cool"
        }
        return weather_data.get(city, f"Weather data not available for {city}")
    
    async def _arun(self, city: str) -> str:
        raise NotImplementedError("Async not implemented")

class NewsTool(BaseTool):
    """Tool for getting news headlines."""
    name = "news"
    description = "Useful for getting latest news headlines. Input can be a topic or 'general' for general news."
    
    def _run(self, topic: str) -> str:
        """Get news for a topic (simulated)."""
        news_data = {
            "tech": "Tech News: AI breakthrough in language models, New smartphone releases, Cloud computing trends",
            "sports": "Sports News: Championship finals this weekend, New record set in athletics, Team transfers",
            "general": "General News: Economic growth reported, Climate summit updates, Education reforms"
        }
        topic_lower = topic.lower()
        for key in news_data:
            if key in topic_lower:
                return news_data[key]
        return news_data["general"]
    
    async def _arun(self, topic: str) -> str:
        raise NotImplementedError("Async not implemented")

# Initialize agent with both tools
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [WeatherTool(), NewsTool()]
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# Test queries
queries = [
    "What's the weather in New York?",
    "What are the latest tech news?",
    "What's the weather in London and what are the top news stories?"
]

for query in queries:
    print(f"\nQuery: {query}")
    print("=" * 70)
    result = agent_executor.invoke({"input": query})
    print(f"\nResult: {result['output']}")
    print("=" * 70)

