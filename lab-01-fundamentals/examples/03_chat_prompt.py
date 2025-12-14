"""
Example: Chat Prompt Templates

This example demonstrates how to use ChatPromptTemplate for
conversational interactions with chat models.
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def chat_prompt_example():
    """Demonstrate chat prompt template usage."""
    
    # Initialize the chat model
    llm_model = os.getenv("LLM_MODEL")

    llm = ChatOpenAI(
        model=llm_model, 
        temperature=0.7, 
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )
    
    # Create a chat prompt template with system and human messages
    system_template = "You are a helpful assistant that explains {subject} in a {tone} way."
    human_template = "Explain {concept} to me."
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", human_template)
    ])
    
    # Format the prompt
    messages = prompt.format_messages(
        subject="programming",
        tone="simple and friendly",
        concept="recursion"
    )
    
    print("Chat Messages:")
    print("-" * 50)
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
    print("-" * 50)
    print("\nLLM Response:")
    print("-" * 50)
    
    # Get response from the chat model
    response = llm.invoke(messages)
    print(response.content)
    print("-" * 50)

if __name__ == "__main__":
    chat_prompt_example()

