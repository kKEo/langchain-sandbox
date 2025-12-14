"""
Example: Simple Chain with LCEL

This example demonstrates how to create and use a basic chain
using LangChain Expression Language (LCEL) to combine prompts and LLMs.
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def simple_chain_example():
    """Demonstrate simple chain usage with LCEL."""
    
    # Initialize the LLM
    llm_model = os.getenv("LLM_MODEL")
    llm = ChatOpenAI(
        model=llm_model, 
        temperature=0.7, 
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["product", "target_audience"],
        template="Write a compelling product description for {product} targeting {target_audience}. "
                 "Highlight key features and benefits in 2-3 sentences."
    )
    
    # Create a chain using LCEL (LangChain Expression Language)
    # The pipe operator | chains the prompt and LLM together
    chain = prompt | llm
    
    # Run the chain
    result = chain.invoke({
        "product": "wireless noise-canceling headphones",
        "target_audience": "professionals who work from home"
    })
    
    print("Product Description:")
    print("-" * 50)
    print(result.content)
    print("-" * 50)
    
    # Run with another example
    result2 = chain.invoke({
        "product": "smart fitness tracker",
        "target_audience": "fitness enthusiasts"
    })
    
    print("\nAnother Product Description:")
    print("-" * 50)
    print(result2.content)
    print("-" * 50)

if __name__ == "__main__":
    simple_chain_example()

