"""
Solution to Exercise 2: Build a Chain for Product Descriptions
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a prompt template for product descriptions
prompt = PromptTemplate(
    input_variables=["product_name", "category", "key_features"],
    template="""Create a compelling product description for marketing purposes.

Product Name: {product_name}
Category: {category}
Key Features: {key_features}

Format your response as follows:
TITLE: [A catchy title]
DESCRIPTION: [A detailed description highlighting benefits and features]
CALL-TO-ACTION: [An engaging call-to-action phrase]

Generate the product description:"""
)

# Create a chain using LCEL (LangChain Expression Language)
chain = prompt | llm

# Sample product data
product_data = {
    "product_name": "EcoWater Pro",
    "category": "Home & Kitchen",
    "key_features": "5-stage filtration, smart monitoring, eco-friendly design"
}

# Run the chain
print("Generating Product Description...")
print("=" * 50)
result = chain.invoke(product_data)

# Print the result
print(result.content)
print("=" * 50)

