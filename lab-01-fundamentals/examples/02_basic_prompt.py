"""
Example: Basic Prompt Template Usage

This example demonstrates how to create and use prompt templates
with LangChain's PromptTemplate class.
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


# Load environment variables
load_dotenv()

def basic_prompt_example():
    """Demonstrate basic prompt template usage."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL"), 
        temperature=0.7, 
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )
    
    # Create a simple prompt template
    template = "Write a {style} story about {topic} in exactly {word_count} words."
    prompt = PromptTemplate.from_template(template)
    
    # Format the prompt with variables
    formatted_prompt = prompt.format(
        style="funny",
        topic="a robot learning to cook",
        word_count="100"
    )
    
    print("Formatted Prompt:")
    print("-" * 50)
    print(formatted_prompt)
    print("-" * 50)
    print("\nLLM Response:")
    print("-" * 50)
    
    # Use the LLM to generate a response
    response = llm.invoke(formatted_prompt)
    print(response.content)
    print("-" * 50)

if __name__ == "__main__":
    basic_prompt_example()

