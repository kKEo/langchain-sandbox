"""
Solution to Exercise 3: Create Summary Memory System
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
    api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    temperature=0.7
)

# Create ConversationSummaryMemory
memory = ConversationSummaryMemory(llm=llm)

# Create ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Simulate a conversation with multiple topics
print("Starting conversation with summary memory...")
print("=" * 70)

exchanges = [
    "I'm planning a vacation to Europe.",
    "I want to visit Paris, London, and Rome.",
    "I'm interested in art museums and historical sites.",
    "I'll be traveling in the summer.",
    "I'm learning French for the trip.",
    "What cities am I visiting and when?"
]

for i, user_input in enumerate(exchanges, 1):
    response = conversation.predict(input=user_input)
    print(f"\nExchange {i}:")
    print(f"User: {user_input}")
    print(f"Assistant: {response}")

# Ask about summarized information
print("\n" + "=" * 70)
print("Asking about earlier information...")
response = conversation.predict(input="What am I learning and why?")
print(f"User: What am I learning and why?")
print(f"Assistant: {response}")

# Display memory summary
print("\n" + "=" * 70)
print("Memory Summary (old conversations summarized):")
print("=" * 70)
print(memory.buffer)

