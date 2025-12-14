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

# TODO: Initialize the LLM
# llm = ...

# TODO: Chain 1 - Generate outline
# outline_prompt = ...
# outline_chain = ...

# TODO: Chain 2 - Expand to blog post
# blog_prompt = ...
# blog_chain = ...

# TODO: Chain 3 - Create social media summary
# summary_prompt = ...
# summary_chain = ...

# TODO: Run the chains sequentially
# First run outline_chain, then use its output for blog_chain, etc.
# outline_result = ...
# blog_result = ...
# summary_result = ...

# TODO: Run the chain with a topic
# topic = "The Future of Artificial Intelligence"
# result = ...

# TODO: Print the results
# print(...)

print("Exercise 3: Complete the code above to create a multi-step chain")

