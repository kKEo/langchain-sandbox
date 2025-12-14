"""
Solution to Exercise 1: Create a Simple Prompt Template
"""
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a prompt template
template = """Create a compelling email subject line for a marketing campaign.

Product: {product_name}
Target Audience: {target_audience}
Urgent Offer: {urgency}

Generate a subject line that is attention-grabbing and relevant to the target audience.
If the offer is urgent, emphasize the urgency in the subject line."""

prompt = PromptTemplate.from_template(template)

# Format the prompt with sample values
formatted_prompt = prompt.format(
    product_name="Premium Coffee Subscription",
    target_audience="coffee enthusiasts",
    urgency="True"
)

print("Formatted Prompt:")
print("-" * 50)
print(formatted_prompt)
print("-" * 50)
print("\nGenerated Subject Line:")
print("-" * 50)

# Get response from LLM
response = llm.invoke(formatted_prompt)
print(response.content)
print("-" * 50)

