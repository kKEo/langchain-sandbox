"""
Example: Simple LLMChain

This example demonstrates how to create and use a basic LLMChain
to combine prompts and LLMs.
"""
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def simple_chain_example():
    """Demonstrate simple LLMChain usage."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["product", "target_audience"],
        template="Write a compelling product description for {product} targeting {target_audience}. "
                 "Highlight key features and benefits in 2-3 sentences."
    )
    
    # Create a chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Run the chain
    result = chain.run(
        product="wireless noise-canceling headphones",
        target_audience="professionals who work from home"
    )
    
    print("Product Description:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    
    # You can also use invoke for more control
    result_dict = chain.invoke({
        "product": "smart fitness tracker",
        "target_audience": "fitness enthusiasts"
    })
    
    print("\nAnother Product Description:")
    print("-" * 50)
    print(result_dict["text"])
    print("-" * 50)

if __name__ == "__main__":
    simple_chain_example()

