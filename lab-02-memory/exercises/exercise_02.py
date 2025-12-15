"""
Exercise 2: Implement Sliding Window Memory

TASK:
Create a chatbot that uses ConversationBufferWindowMemory to keep only
the most recent exchanges. This is useful for long conversations where
you want to limit memory size.

INSTRUCTIONS:
1. Use ConversationBufferWindowMemory with k=3 (keep last 3 exchanges)
2. Create a conversation chain
3. Simulate a conversation with 6+ exchanges
4. Verify that only the last 3 exchanges are in memory
5. Ask a question about information from an early exchange (should not be remembered)

HINT: Set k parameter in ConversationBufferWindowMemory
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TODO: Import necessary modules
# from langchain...

# TODO: Initialize the LLM
# llm = ...

# TODO: Create ConversationBufferWindowMemory with k=3
# memory = ...

# TODO: Create ConversationChain
# conversation = ...

# TODO: Simulate a longer conversation (6+ exchanges)
# Include information in early exchanges that won't be remembered

# TODO: Display memory contents to verify only last 3 exchanges are kept

print("Exercise 2: Complete the code above to implement sliding window memory")

