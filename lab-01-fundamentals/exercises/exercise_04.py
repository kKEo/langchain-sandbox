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

# TODO: Import necessary modules
# from langchain...

# TODO: Create output parser
# parser = ...

# TODO: Initialize the LLM
# llm = ...

# TODO: Create prompt template with format instructions
# prompt = ...

# TODO: Create chain using pipe operator
# chain = ...

# TODO: Run the chain with a book title
# book_title = "1984 by George Orwell"
# result = ...

# TODO: Print structured output
# print(...)

print("Exercise 4: Complete the code above to parse structured outputs")

