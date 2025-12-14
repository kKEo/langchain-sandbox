"""
Solution to Exercise 3: Implement a Multi-Step Chain
"""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Chain 1 - Generate outline
outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Create a detailed blog post outline for the topic: {topic}. "
             "Include 5-7 main sections with brief descriptions for each."
)
outline_chain = outline_prompt | llm

# Chain 2 - Expand to blog post
blog_prompt = PromptTemplate(
    input_variables=["outline"],
    template="Using the following outline, write a full blog post (approximately 500 words):\n\n{outline}\n\nBlog Post:"
)
blog_chain = blog_prompt | llm

# Chain 3 - Create social media summary
summary_prompt = PromptTemplate(
    input_variables=["blog_post"],
    template="Create a concise social media summary (2-3 sentences) for the following blog post:\n\n{blog_post}\n\nSocial Media Summary:"
)
summary_chain = summary_prompt | llm

# Run the chain with a topic
topic = "The Future of Artificial Intelligence"
print(f"Running Multi-Step Chain for topic: {topic}")
print("=" * 70)

# Step 1: Generate outline
outline_result = outline_chain.invoke({"topic": topic})
outline = outline_result.content

# Step 2: Expand to blog post
blog_result = blog_chain.invoke({"outline": outline})
blog_post = blog_result.content

# Step 3: Create social media summary
summary_result = summary_chain.invoke({"blog_post": blog_post})
summary = summary_result.content

# Print the results
print("\n" + "=" * 70)
print("OUTLINE:")
print("-" * 70)
print(outline)
print("\n" + "=" * 70)
print("BLOG POST:")
print("-" * 70)
print(blog_post)
print("\n" + "=" * 70)
print("SOCIAL MEDIA SUMMARY:")
print("-" * 70)
print(summary)
print("=" * 70)

