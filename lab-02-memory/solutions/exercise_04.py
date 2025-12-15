"""
Solution to Exercise 4: Customer Support Assistant with Context Retention
"""
import os
from dotenv import load_dotenv
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
    api_key=os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    temperature=0.7
)

# Create ConversationSummaryBufferMemory
memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=150,  # Summarize when buffer exceeds this
    memory_key="chat_history",
    return_messages=True
)

# Create a prompt template with system message for customer support
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support assistant. Be professional, "
     "empathetic, and solution-oriented. Remember customer details and issues."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create a chain using LCEL
chain = prompt | llm

# Simulate a customer support conversation
print("Starting customer support conversation...")
print("=" * 70)

exchanges = [
    "Hi, I'm John Smith and I'm having trouble with my account login.",
    "I keep getting an error message that says 'Invalid credentials'.",
    "I've tried resetting my password multiple times.",
    "My email is john.smith@email.com.",
    "I last logged in successfully about a week ago.",
    "Can you help me resolve this issue?",
    "What's my email address and what problem am I experiencing?"
]

for i, user_input in enumerate(exchanges, 1):
    # Load memory variables
    memory_variables = memory.load_memory_variables({})
    
    # Invoke chain with memory
    response = chain.invoke({
        "input": user_input,
        "chat_history": memory_variables["chat_history"]
    })
    
    # Save to memory
    memory.save_context({"input": user_input}, {"output": response.content})
    
    print(f"\nExchange {i}:")
    print(f"Customer: {user_input}")
    print(f"Support: {response.content}")

# Display memory to see summary + recent messages
print("\n" + "=" * 70)
print("Memory Contents (summary + recent messages):")
print("=" * 70)
print(memory.buffer)

