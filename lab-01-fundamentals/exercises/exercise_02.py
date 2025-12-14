"""
Exercise 2: Build a Chain for Product Descriptions

TASK:
Create an LLMChain that generates and formats product descriptions.
The chain should:
1. Accept product name, category, and key features
2. Generate a compelling product description
3. Format it as a structured output with title, description, and call-to-action

INSTRUCTIONS:
1. Import LLMChain and necessary modules
2. Create a prompt template that includes all required information
3. Create an LLMChain combining the prompt and LLM
4. Run the chain with sample product data
5. Display the formatted output

HINT: Use LLMChain(llm=llm, prompt=prompt) to create the chain
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain...

# TODO: Initialize the LLM
# llm = ...

# TODO: Create a prompt template for product descriptions
# The template should include: product_name, category, key_features
# prompt = ...

# TODO: Create an LLMChain
# chain = ...

# Sample product data
product_data = {
    "product_name": "EcoWater Pro",
    "category": "Home & Kitchen",
    "key_features": "5-stage filtration, smart monitoring, eco-friendly design"
}

# TODO: Run the chain with the product data
# result = ...

# TODO: Print the result
# print(...)

print("Exercise 2: Complete the code above to generate product descriptions")

