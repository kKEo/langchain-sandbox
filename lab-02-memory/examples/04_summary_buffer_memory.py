"""
Example: Conversation Summary Buffer Memory

This example demonstrates how to use ConversationSummaryBufferMemory
to combine summary of old messages with recent message buffer.
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def summary_buffer_memory_example():
    """Demonstrate conversation summary buffer memory."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        temperature=0.7
    )
    
    # Create summary buffer memory (max_token_limit controls when to summarize)
    memory = ConversationSummaryBufferMemory(
        llm=llm,
        max_token_limit=100,  # Summarize when buffer exceeds this
        return_messages=True
    )
    
    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    # Simulate a longer conversation
    print("Starting conversation with summary buffer memory...")
    print("=" * 70)
    
    exchanges = [
        "I'm learning machine learning.",
        "I've completed courses on supervised learning.",
        "Now I'm studying neural networks and deep learning.",
        "I want to build a computer vision project.",
        "Can you help me with image classification?",
        "What have I been learning about?"
    ]
    
    for i, user_input in enumerate(exchanges, 1):
        response = conversation.predict(input=user_input)
        print(f"\nExchange {i}:")
        print(f"User: {user_input}")
        print(f"Assistant: {response}")
    
    # Display memory contents
    print("\n" + "=" * 70)
    print("Memory Contents (summary + recent messages):")
    print("=" * 70)
    print(memory.buffer)

if __name__ == "__main__":
    summary_buffer_memory_example()

