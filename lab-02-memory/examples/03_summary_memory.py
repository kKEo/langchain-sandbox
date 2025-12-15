"""
Example: Conversation Summary Memory

This example demonstrates how to use ConversationSummaryMemory
to summarize old conversations while maintaining context.
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def summary_memory_example():
    """Demonstrate conversation summary memory."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        temperature=0.7
    )
    
    # Create summary memory
    memory = ConversationSummaryMemory(llm=llm)
    
    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    # Simulate a conversation
    print("Starting conversation with summary memory...")
    print("=" * 70)
    
    exchanges = [
        "I'm planning a trip to Japan next month.",
        "I want to visit Tokyo, Kyoto, and Osaka.",
        "I'm interested in traditional temples and modern technology.",
        "What cities am I visiting and what am I interested in?"
    ]
    
    for i, user_input in enumerate(exchanges, 1):
        response = conversation.predict(input=user_input)
        print(f"\nExchange {i}:")
        print(f"User: {user_input}")
        print(f"Assistant: {response}")
    
    # Display memory summary
    print("\n" + "=" * 70)
    print("Memory Summary:")
    print("=" * 70)
    print(memory.buffer)

if __name__ == "__main__":
    summary_memory_example()

