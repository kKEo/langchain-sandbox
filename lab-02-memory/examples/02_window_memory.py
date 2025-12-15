"""
Example: Conversation Buffer Window Memory

This example demonstrates how to use ConversationBufferWindowMemory
to keep only the most recent exchanges in memory.
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def window_memory_example():
    """Demonstrate conversation buffer window memory."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        temperature=0.7
    )
    
    # Create window memory (keep last 2 exchanges)
    memory = ConversationBufferWindowMemory(k=2, return_messages=True)
    
    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    # Simulate a longer conversation
    print("Starting conversation with window memory (k=2)...")
    print("=" * 70)
    
    exchanges = [
        "Hi, I'm Bob and I work as a software engineer.",
        "I specialize in backend development.",
        "I use Python and Go for my projects.",
        "What programming languages do I use?"
    ]
    
    for i, user_input in enumerate(exchanges, 1):
        response = conversation.predict(input=user_input)
        print(f"\nExchange {i}:")
        print(f"User: {user_input}")
        print(f"Assistant: {response}")
    
    # Display memory contents (only last 2 exchanges)
    print("\n" + "=" * 70)
    print("Memory Contents (last 2 exchanges only):")
    print("=" * 70)
    print(memory.buffer)

if __name__ == "__main__":
    window_memory_example()

