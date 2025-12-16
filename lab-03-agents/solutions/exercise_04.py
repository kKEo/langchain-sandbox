"""
Solution to Exercise 4: Custom Database Query Tool
"""
import os
from dotenv import load_dotenv
from langchain.tools import BaseTool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Sample data (simulated database)
users = [
    {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
    {"id": 2, "name": "Bob", "age": 25, "city": "London"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Tokyo"},
    {"id": 4, "name": "Diana", "age": 28, "city": "New York"},
    {"id": 5, "name": "Eve", "age": 32, "city": "Paris"}
]

class DatabaseTool(BaseTool):
    """Tool for querying a simulated database."""
    name = "database"
    description = """Useful for querying user database. 
    Input should be a natural language query about users.
    Examples: 'all users', 'users in New York', 'users older than 28'"""
    
    def _run(self, query: str) -> str:
        """Query the database (simulated)."""
        query_lower = query.lower()
        results = []
        
        try:
            # Simple query parsing
            if "all" in query_lower or "every" in query_lower:
                results = users
            elif "new york" in query_lower:
                results = [u for u in users if u["city"] == "New York"]
            elif "london" in query_lower:
                results = [u for u in users if u["city"] == "London"]
            elif "tokyo" in query_lower:
                results = [u for u in users if u["city"] == "Tokyo"]
            elif "older" in query_lower or "age" in query_lower:
                # Extract age threshold
                import re
                age_match = re.search(r'(\d+)', query)
                if age_match:
                    threshold = int(age_match.group(1))
                    results = [u for u in users if u["age"] > threshold]
                else:
                    results = users
            elif "younger" in query_lower:
                import re
                age_match = re.search(r'(\d+)', query)
                if age_match:
                    threshold = int(age_match.group(1))
                    results = [u for u in users if u["age"] < threshold]
                else:
                    results = users
            else:
                # Default: return all
                results = users
            
            if not results:
                return "No users found matching the query."
            
            # Format results
            formatted = "\n".join([
                f"ID: {u['id']}, Name: {u['name']}, Age: {u['age']}, City: {u['city']}"
                for u in results
            ])
            return f"Found {len(results)} user(s):\n{formatted}"
            
        except Exception as e:
            return f"Database query error: {str(e)}"
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")

# Initialize agent with database tool
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = initialize_agent(
    tools=[DatabaseTool()],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Test queries
queries = [
    "Query the database for all users",
    "Find users older than 28",
    "What users are in New York?"
]

for query in queries:
    print(f"\nQuery: {query}")
    print("=" * 70)
    result = agent.run(query)
    print(f"\nResult: {result}")
    print("=" * 70)

