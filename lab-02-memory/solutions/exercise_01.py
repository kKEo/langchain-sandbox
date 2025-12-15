"""
Solution to Exercise 1: Build a Chatbot with Conversation History
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
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

# Create ConversationBufferMemory
memory = ConversationBufferMemory()

# Create ConversationChain with memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Simulate a conversation
print("Starting conversation...")
print("=" * 70)

# Exchange 1: User introduces themselves
response1 = conversation.predict(input="Hi, my name is Sarah and I'm a data scientist.")
print(f"\nUser: Hi, my name is Sarah and I'm a data scientist.")
print(f"Assistant: {response1}")

# Exchange 2: User shares a preference
response2 = conversation.predict(input="I love working with Python and machine learning.")
print(f"\nUser: I love working with Python and machine learning.")
print(f"Assistant: {response2}")

# Exchange 3: User asks a question
response3 = conversation.predict(input="Can you recommend a good ML library?")
print(f"\nUser: Can you recommend a good ML library?")
print(f"Assistant: {response3}")

# Exchange 4: User asks about previous information
response4 = conversation.predict(input="What's my name and what do I do?")
print(f"\nUser: What's my name and what do I do?")
print(f"Assistant: {response4}")

# Display conversation history
print("\n" + "=" * 70)
print("Full Conversation History:")
print("=" * 70)
print(memory.buffer)

