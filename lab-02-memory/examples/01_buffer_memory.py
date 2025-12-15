"""
Example: Conversation Buffer Memory

This example demonstrates how to use ConversationBufferMemory
to store complete conversation history.
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def buffer_memory_example():
    """Demonstrate conversation buffer memory."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        temperature=0.7
    )
    
    # Create buffer memory
    memory = ConversationBufferMemory()
    
    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    # Simulate a conversation
    print("Starting conversation with buffer memory...")
    print("=" * 70)
    
    response1 = conversation.predict(input="Hi, my name is Alice. I love Python programming.")
    print(f"\nUser: Hi, my name is Alice. I love Python programming.")
    print(f"Assistant: {response1}")
    
    response2 = conversation.predict(input="What's my name and what do I like?")
    print(f"\nUser: What's my name and what do I like?")
    print(f"Assistant: {response2}")
    
    response3 = conversation.predict(input="Can you recommend a Python library for data analysis?")
    print(f"\nUser: Can you recommend a Python library for data analysis?")
    print(f"Assistant: {response3}")
    
    # Display memory contents
    print("\n" + "=" * 70)
    print("Memory Contents:")
    print("=" * 70)
    print(memory.buffer)

if __name__ == "__main__":
    buffer_memory_example()

