"""
Exercise 1: Create a Simple Prompt Template

TASK:
Create a prompt template that generates personalized email subject lines
for marketing campaigns. The template should accept:
- product_name: The name of the product being promoted
- target_audience: The target customer segment
- urgency: Whether the offer is urgent (True/False)

INSTRUCTIONS:
1. Import necessary modules (PromptTemplate, ChatOpenAI)
2. Create a prompt template with the variables above
3. Initialize a ChatOpenAI model
4. Format and run the prompt with sample values
5. Print the generated subject line

HINT: Use PromptTemplate.from_template() or PromptTemplate() constructor
"""
import os
from dotenv import load_dotenv
load_dotenv()

# TODO: Import necessary modules
# from langchain...
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# TODO: Create your prompt template here
template = PromptTemplate(
    input_variables=["product_name", "target_audience", "urgency"],
    template="""
    Create a compelling email subject line for a marketing campaign. 
    Product: {product_name} 
    Target Audience: {target_audience} 
    Urgent Offer: {urgency}

    Generate a subject line that is attention-grabbing and appropriate for the target audience.
    """
)

# TODO: Initialize the LLM
# llm = ...
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# TODO: Format the prompt with sample values
# formatted_prompt = ...
formatted_prompt = template.format(
    product_name="Premium Coffee Subscription",
    target_audience="coffee enthusiasts",
    urgency="True"
)
# TODO: Get response from LLM and print it
# response = ...
response = llm.invoke(formatted_prompt)
print(response.content)
print("-" * 50)
print("Exercise 1: Complete the code above to generate email subject lines")
