"""
Solution to Exercise 2: Implement Sliding Window Memory
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferWindowMemory
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

# Create ConversationBufferWindowMemory with k=3
memory = ConversationBufferWindowMemory(k=3, return_messages=True)

# Create ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Simulate a longer conversation
print("Starting conversation with window memory (k=3)...")
print("=" * 70)

exchanges = [
    "Hi, I'm Tom and I'm a teacher.",
    "I teach mathematics at a high school.",
    "I've been teaching for 10 years.",
    "I also coach the school's basketball team.",
    "My favorite subject to teach is calculus.",
    "What do I teach and for how long?"
]

for i, user_input in enumerate(exchanges, 1):
    response = conversation.predict(input=user_input)
    print(f"\nExchange {i}:")
    print(f"User: {user_input}")
    print(f"Assistant: {response}")

# Try to ask about early information (should not be remembered)
print("\n" + "=" * 70)
print("Asking about early information (name)...")
response = conversation.predict(input="What's my name?")
print(f"User: What's my name?")
print(f"Assistant: {response}")
print("\nNote: The name 'Tom' from exchange 1 is no longer in memory!")

# Display memory contents
print("\n" + "=" * 70)
print("Memory Contents (last 3 exchanges only):")
print("=" * 70)
print(memory.buffer)

