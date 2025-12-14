"""
Exercise 4: Parse Structured Outputs with Pydantic

TASK:
Create a chain that generates a book review and parses it into a structured format.
The output should include:
- title: Book title
- rating: Rating out of 5
- pros: List of positive aspects
- cons: List of negative aspects
- recommendation: Boolean indicating if recommended

INSTRUCTIONS:
1. Define a Pydantic model for the book review structure
2. Create a PydanticOutputParser
3. Create a prompt template that includes format instructions
4. Build a chain: prompt | llm | parser
5. Run with a book title and display the structured output

HINT: Use parser.get_format_instructions() in your prompt template
      Use the pipe operator (|) to chain: prompt | llm | parser
"""
import os
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# TODO: Define Pydantic model for BookReview
# class BookReview(BaseModel):
#     ...
class BookReview(BaseModel):
    title: str = Field(description="The title of the book")
    rating: int = Field(description="The rating of the book out of 5")
    pros: List[str] = Field(description="The positive aspects of the book")
    cons: List[str] = Field(description="The negative aspects of the book")
    recommendation: bool = Field(description="Whether the book is recommended")

# TODO: Import necessary modules
# from langchain...
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# TODO: Create output parser
# parser = ...
parser = PydanticOutputParser(pydantic_object=BookReview)

# TODO: Initialize the LLM
# llm = ...
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)
# TODO: Create prompt template with format instructions
# prompt = ...
template="""
      Write a comprehensive book review for: {book_title}. 
      
      {format_instructions}

      Include the title, rating, pros, cons, and recommendation:
      """
instructions = parser.get_format_instructions()
print("Instructions: ")
print(f"{instructions}")

prompt = PromptTemplate(
    input_variables=["book_title"],
    template=template,
    partial_variables={"format_instructions": instructions}
)
# TODO: Create chain using pipe operator
# chain = ...
chain = prompt | llm | parser

# TODO: Run the chain with a book title
# book_title = "1984 by George Orwell"
# result = ...
book_title = "1984 by George Orwell"

print("Genereting review...")

result = chain.invoke({"book_title": book_title})

# TODO: Print structured output
# print(...)
  # Print structured output
print("=== REVIEW ===")
print("=" * 70)
print(f"Title: {result.title}")
print(f"Rating: {result.rating} out of 5")
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


print("Exercise 4: Complete the code above to parse structured outputs")

