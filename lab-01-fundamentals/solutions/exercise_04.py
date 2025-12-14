"""
Solution to Exercise 4: Parse Structured Outputs with Pydantic
"""
import os
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define Pydantic model for BookReview
class BookReview(BaseModel):
    """A structured book review."""
    title: str = Field(description="The title of the book")
    rating: int = Field(description="Rating out of 5 stars", ge=1, le=5)
    pros: List[str] = Field(description="List of positive aspects of the book")
    cons: List[str] = Field(description="List of negative aspects or areas for improvement")
    recommendation: bool = Field(description="Whether the book is recommended")

# Create output parser
parser = PydanticOutputParser(pydantic_object=BookReview)

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create prompt template with format instructions
prompt = PromptTemplate(
    template="""Write a comprehensive book review for: {book_title}

{format_instructions}

Provide a detailed review with rating, pros, cons, and recommendation:""",
    input_variables=["book_title"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Create chain using pipe operator
chain = prompt | llm | parser

# Run the chain with a book title
book_title = "1984 by George Orwell"
print(f"Generating structured book review for: {book_title}")
print("=" * 70)

try:
    result = chain.invoke({"book_title": book_title})
    
    # Print structured output
    print("\nSTRUCTURED BOOK REVIEW:")
    print("=" * 70)
    print(f"Title: {result.title}")
    print(f"Rating: {result.rating}/5")
    print(f"\nPros:")
    for pro in result.pros:
        print(f"  • {pro}")
    print(f"\nCons:")
    for con in result.cons:
        print(f"  • {con}")
    print(f"\nRecommended: {'Yes' if result.recommendation else 'No'}")
    print("=" * 70)
    
    # Also show as dictionary
    print("\nAs Dictionary:")
    print(result.dict())
    
except Exception as e:
    print(f"Error: {e}")
    print("\nNote: If parsing fails, the LLM output may not match the expected format.")
    print("Try running again or adjust the prompt to be more explicit about the format.")

