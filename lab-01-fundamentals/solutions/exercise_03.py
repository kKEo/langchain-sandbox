"""
Solution to Exercise 3: Implement a Multi-Step Chain
"""
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
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
outline_chain = LLMChain(
    llm=llm,
    prompt=outline_prompt,
    output_key="outline"
)

# Chain 2 - Expand to blog post
blog_prompt = PromptTemplate(
    input_variables=["outline"],
    template="Using the following outline, write a full blog post (approximately 500 words):\n\n{outline}\n\nBlog Post:"
)
blog_chain = LLMChain(
    llm=llm,
    prompt=blog_prompt,
    output_key="blog_post"
)

# Chain 3 - Create social media summary
summary_prompt = PromptTemplate(
    input_variables=["blog_post"],
    template="Create a concise social media summary (2-3 sentences) for the following blog post:\n\n{blog_post}\n\nSocial Media Summary:"
)
summary_chain = LLMChain(
    llm=llm,
    prompt=summary_prompt,
    output_key="summary"
)

# Create sequential chain
sequential_chain = SequentialChain(
    chains=[outline_chain, blog_chain, summary_chain],
    input_variables=["topic"],
    output_variables=["outline", "blog_post", "summary"],
    verbose=True
)

# Run the chain with a topic
topic = "The Future of Artificial Intelligence"
print(f"Running Multi-Step Chain for topic: {topic}")
print("=" * 70)

result = sequential_chain({"topic": topic})

# Print the results
print("\n" + "=" * 70)
print("OUTLINE:")
print("-" * 70)
print(result["outline"])
print("\n" + "=" * 70)
print("BLOG POST:")
print("-" * 70)
print(result["blog_post"])
print("\n" + "=" * 70)
print("SOCIAL MEDIA SUMMARY:")
print("-" * 70)
print(result["summary"])
print("=" * 70)

