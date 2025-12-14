"""
Exercise 2: Build a Chain for Product Descriptions

TASK:
Create a chain using LCEL (LangChain Expression Language) that generates and formats product descriptions.
The chain should:
1. Accept product name, category, and key features
2. Generate a compelling product description
3. Format it as a structured output with title, description, and call-to-action

INSTRUCTIONS:
1. Import necessary modules (PromptTemplate, ChatOpenAI)
2. Create a prompt template that includes all required information
3. Create a chain using LCEL by combining the prompt and LLM with the pipe operator (|)
4. Run the chain with sample product data
5. Display the formatted output

HINT: Use the pipe operator to create a chain: chain = prompt | llm
      Then invoke it with: result = chain.invoke(product_data)
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain...
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# TODO: Initialize the LLM
# llm = ...
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)
# TODO: Create a prompt template for product descriptions
# The template should include: product_name, category, key_features
# prompt = ...
prompt = PromptTemplate(
    input_variables=["product_name", "category", "key_features"],
    template="""
    Create a compelling product description for marketing purposes.
    Product Name: {product_name}
    Category: {category}
    Key Features: {key_features}

    Generate a product description that is attention-grabbing and 
    appropriate for the target audience. Format your response as follows:
    TITLE: [A catchy title]
    DESCRIPTION: [A detailed description highlighting benefits and features]
    CALL-TO-ACTION: [An engaging call-to-action phrase]
    """
)
# TODO: Create a chain using LCEL (pipe operator)
# chain = ...
chain = prompt | llm


product_data = {
    "product_name": "EcoWater Pro",
    "category": "Home & Kitchen",
    "key_features": "5-stage filtration, smart monitoring, eco-friendly design"
}

# TODO: Run the chain with the product data
# result = ...
print("Generating Product Description...")
result = chain.invoke(product_data)

# TODO: Print the result
# print(...)
print(result.content)
print("-" * 50)
print("Exercise 2: Complete the code above to generate product descriptions")

