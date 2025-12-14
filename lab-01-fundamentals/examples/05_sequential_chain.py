"""
Example: Sequential Chains

This example demonstrates how to create multi-step chains where
the output of one chain becomes the input of the next.
"""
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def sequential_chain_example():
    """Demonstrate sequential chain usage."""
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # Step 1: Generate a story
    story_template = "Write a short {genre} story about {topic} in 100 words."
    story_prompt = PromptTemplate(
        input_variables=["genre", "topic"],
        template=story_template
    )
    story_chain = LLMChain(llm=llm, prompt=story_prompt, output_key="story")
    
    # Step 2: Summarize the story
    summary_template = "Summarize the following story in one sentence:\n\n{story}"
    summary_prompt = PromptTemplate(
        input_variables=["story"],
        template=summary_template
    )
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")
    
    # Step 3: Create a title
    title_template = "Create a catchy title for this story summary: {summary}"
    title_prompt = PromptTemplate(
        input_variables=["summary"],
        template=title_template
    )
    title_chain = LLMChain(llm=llm, prompt=title_prompt, output_key="title")
    
    # Create a sequential chain
    sequential_chain = SimpleSequentialChain(
        chains=[story_chain, summary_chain, title_chain],
        verbose=True  # Set to True to see intermediate steps
    )
    
    # Run the chain
    print("Running Sequential Chain:")
    print("=" * 50)
    result = sequential_chain.run(
        genre="sci-fi",
        topic="time travel"
    )
    
    print("\n" + "=" * 50)
    print("Final Result (Title):")
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    sequential_chain_example()

