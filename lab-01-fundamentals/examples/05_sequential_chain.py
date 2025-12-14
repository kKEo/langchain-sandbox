"""
Example: Sequential Chains with LCEL

This example demonstrates how to create multi-step chains using LCEL where
the output of one chain becomes the input of the next.
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def sequential_chain_example():
    """Demonstrate sequential chain usage with LCEL."""
    
    # Initialize the LLM
    llm_model = os.getenv("LLM_MODEL")
    llm = ChatOpenAI(
        model=llm_model, 
        temperature=0.7, 
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )
    
    # Step 1: Generate a story
    story_template = "Write a short {genre} story about {topic} in 100 words."
    story_prompt = PromptTemplate(
        input_variables=["genre", "topic"],
        template=story_template
    )
    story_chain = story_prompt | llm
    
    # Step 2: Summarize the story
    summary_template = "Summarize the following story in one sentence:\n\n{story}"
    summary_prompt = PromptTemplate(
        input_variables=["story"],
        template=summary_template
    )
    summary_chain = summary_prompt | llm
    
    # Step 3: Create a title
    title_template = "Create a catchy title for this story summary: {summary}"
    title_prompt = PromptTemplate(
        input_variables=["summary"],
        template=title_template
    )
    title_chain = title_prompt | llm
    
    # Create a sequential chain using LCEL
    # Each step passes its output to the next using RunnablePassthrough
    def extract_story(inputs):
        """Extract story content from the first chain's output."""
        return {"story": inputs.content}
    
    def extract_summary(inputs):
        """Extract summary content from the second chain's output."""
        return {"summary": inputs.content}
    
    # Build the sequential chain
    sequential_chain = (
        story_chain
        | RunnablePassthrough.assign(story_text=lambda x: x.content)
        | (lambda x: {"story": x["story_text"]})
        | summary_chain
        | RunnablePassthrough.assign(summary_text=lambda x: x.content)
        | (lambda x: {"summary": x["summary_text"]})
        | title_chain
    )
    
    # Run the chain
    print("Running Sequential Chain:")
    print("=" * 50)
    
    # For cleaner execution, we'll run step by step to show intermediate results
    story_result = story_chain.invoke({"genre": "sci-fi", "topic": "time travel"})
    story_text = story_result.content
    print(f"Story: {story_text}\n")
    
    summary_result = summary_chain.invoke({"story": story_text})
    summary_text = summary_result.content
    print(f"Summary: {summary_text}\n")
    
    title_result = title_chain.invoke({"summary": summary_text})
    result = title_result.content
    print(f"Title: {result}\n")
    
    print("=" * 50)
    print("Final Result (Title):")
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    sequential_chain_example()

