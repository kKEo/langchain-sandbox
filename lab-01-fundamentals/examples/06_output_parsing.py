"""
Example: Output Parsing

This example demonstrates how to parse structured outputs from LLMs
using Pydantic models and output parsers.
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List

# Load environment variables
load_dotenv()

# Define a Pydantic model for structured output
class Recipe(BaseModel):
    """A recipe with structured information."""
    name: str = Field(description="The name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    steps: List[str] = Field(description="Step-by-step cooking instructions")
    prep_time: int = Field(description="Preparation time in minutes")
    cook_time: int = Field(description="Cooking time in minutes")
    difficulty: str = Field(description="Difficulty level: easy, medium, or hard")

def output_parsing_example():
    """Demonstrate output parsing with Pydantic."""
    
    # Initialize the LLM
    llm = ChatOpenAI(
        model= os.getenv("LLM_MODEL"), 
        temperature=0.7, 
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )
    
    # Create the output parser
    parser = PydanticOutputParser(pydantic_object=Recipe)
    
    # Create a prompt template that includes format instructions
    template = """Create a recipe for {dish}.

{format_instructions}

Provide the recipe details:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["dish"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    # Create a chain
    chain = prompt | llm | parser
    
    # Run the chain
    print("Generating Recipe...")
    print("=" * 50)
    
    try:
        recipe = chain.invoke({"dish": "chocolate chip cookies"})
        
        print("\nParsed Recipe:")
        print("=" * 50)
        print(f"Name: {recipe.name}")
        print(f"\nIngredients:")
        for ingredient in recipe.ingredients:
            print(f"  - {ingredient}")
        print(f"\nSteps:")
        for i, step in enumerate(recipe.steps, 1):
            print(f"  {i}. {step}")
        print(f"\nPrep Time: {recipe.prep_time} minutes")
        print(f"Cook Time: {recipe.cook_time} minutes")
        print(f"Difficulty: {recipe.difficulty}")
        print("=" * 50)
        
        # Access as dictionary
        print("\nAs Dictionary:")
        print(recipe.dict())
        
    except Exception as e:
        print(f"Error parsing output: {e}")
        print("\nThis can happen if the LLM output doesn't match the expected format.")
        print("Try running again or adjust the prompt.")

if __name__ == "__main__":
    output_parsing_example()

