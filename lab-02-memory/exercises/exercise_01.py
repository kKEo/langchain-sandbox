"""
Exercise 1: Build a Chatbot with Conversation History

TASK:
Create a simple chatbot that maintains conversation history using
ConversationBufferMemory. The chatbot should:
1. Remember user's name and preferences
2. Reference previous messages in responses
3. Display the conversation history at the end

INSTRUCTIONS:
1. Import ConversationBufferMemory and ConversationChain
2. Initialize the LLM and memory
3. Create a ConversationChain with memory
4. Simulate a conversation with at least 4 exchanges
5. Display the full conversation history

HINT: Use ConversationChain with memory parameter
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain...
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


# TODO: Initialize the LLM
# llm = ...
llm = ChatOpenAI(
    model = os.getenv("LLM_MODEL"),
    api_key = os.getenv("LLM_API_KEY"),
    base_url = os.getenv("LLM_BASE_URL"),
    temperature = 0.7
)

# TODO: Create ConversationBufferMemory
# memory = ...
memory = ConversationBufferMemory()

# TODO: Create ConversationChain with memory
# conversation = ...
conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose = True
)

for exchange in (
    "I'm Dino, little dinosaur",
    "I'm a replitle, I eat small mammals",
    "Do you know where i can find jummy chanks?"
    "What is my favourite food?"
    ):
        resp = conversation.predict(input=exchange)
        print(f"User: {exchange}")
        print(f"Assistant: {resp}")

print(memory.buffer)

# TODO: Simulate a conversation
# Exchange 1: User introduces themselves
# Exchange 2: User shares a preference
# Exchange 3: User asks a question
# Exchange 4: User asks about previous information

# TODO: Display conversation history
# print(memory.buffer)

print("Exercise 1: Complete the code above to build a chatbot with memory")

