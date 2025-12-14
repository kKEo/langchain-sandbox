"""
Exercise 3: Implement a Multi-Step Chain

TASK:
Create a multi-step chain using LCEL that:
1. Generates a blog post outline on a given topic
2. Expands the outline into a full blog post
3. Creates a social media summary of the blog post

INSTRUCTIONS:
1. Create three separate chains using LCEL:
   - Chain 1: Generate outline (input: topic, output: outline)
   - Chain 2: Expand outline (input: outline, output: blog_post)
   - Chain 3: Create summary (input: blog_post, output: summary)
2. Run each chain sequentially, passing outputs from one to the next
3. Run with a sample topic
4. Display all outputs

HINT: Use the pipe operator to create each chain: chain = prompt | llm
      Extract content from results: result.content
      Pass outputs between chains manually or use RunnablePassthrough for more complex flows
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
# TODO: Chain 1 - Generate outline
# outline_prompt = ...
# outline_chain = ...

outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Create a detailed blog post outline for the topic: {topic}. "
             "Include 5-7 main sections with brief descriptions for each."
)
outline_chain = outline_prompt | llm

# TODO: Chain 2 - Expand to blog post
# blog_prompt = ...
# blog_chain = ...

blog_prompt = PromptTemplate(
    input_variables=["outline"],
    template="Using the following outline, write a full blog post (approximately 500 words):\n\n{outline}\n\nBlog Post:"
)
blog_chain = blog_prompt | llm

# TODO: Chain 3 - Create social media summary
# summary_prompt = ...
# summary_chain = ...

summary_prompt = PromptTemplate(
    input_variables=["blog_post"],
    template="Create a concise social media summary (2-3 sentences) for the following blog post:\n\n{blog_post}\n\nSocial Media Summary:"
)
summary_chain = summary_prompt | llm

# TODO: Run the chains sequentially
# First run outline_chain, then use its output for blog_chain, etc.
# outline_result = ...
# blog_result = ...
# summary_result = ...
topic = "The Future of Combustion Engine Cars"
print(f"Creating blog post outline for topic: {topic}")
print("Thinking...")
outline_result = outline_chain.invoke({"topic": topic})
blog_result = blog_chain.invoke({"outline": outline_result.content})
summary_result = summary_chain.invoke({"blog_post": blog_result.content})

print(outline_result.content)
print("-" * 50)
print(blog_result.content)
print("-" * 50)
print(summary_result.content)
print("-" * 50)
# TODO: Run the chain with a topic

# result = ...
print(f"Running Multi-Step Chain for topic: {topic}")
print("=" * 70)

# TODO: Print the results
# print(...)

print("Exercise 3: Complete the code above to create a multi-step chain")

