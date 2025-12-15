"""
Example: Using Memory with Custom Chains

This example demonstrates how to integrate memory into custom chains
using LCEL (LangChain Expression Language).
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def memory_in_chain_example():
    """Demonstrate using memory with custom chains using LCEL."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        temperature=0.7
    )
    
    # Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create a prompt template that includes chat history
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that remembers previous conversations."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    
    # Create a chain using LCEL
    chain = prompt | llm
    
    # Simulate a conversation
    print("Starting conversation with custom chain and memory...")
    print("=" * 70)
    
    user_inputs = [
        "My favorite color is blue.",
        "I also like green.",
        "What are my favorite colors?"
    ]
    
    for user_input in user_inputs:
        # Load memory variables
        memory_variables = memory.load_memory_variables({})
        
        # Invoke chain with memory
        response = chain.invoke({
            "input": user_input,
            "chat_history": memory_variables["chat_history"]
        })
        
        # Save to memory
        memory.save_context({"input": user_input}, {"output": response.content})
        
        print(f"\nUser: {user_input}")
        print(f"Assistant: {response.content}")
    
    # Display memory
    print("\n" + "=" * 70)
    print("Chat History:")
    print("=" * 70)
    for message in memory.chat_memory.messages:
        print(f"{message.__class__.__name__}: {message.content}")

if __name__ == "__main__":
    memory_in_chain_example()

