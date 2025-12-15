# Lab 2: Memory and Conversation Management

**Level: Moderate-Intermediate**

## Learning Objectives

By the end of this lab, you will be able to:
- Implement conversation memory to maintain context
- Understand different memory types and their use cases
- Build conversational chains with state management
- Handle multi-turn conversations effectively

## Prerequisites

- Completion of Lab 1 (or equivalent knowledge)
- Understanding of chains and prompts
- Basic knowledge of state management

## Setup

1. Install lab-specific dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your API keys are set (from Lab 1):
   ```bash
   export LLM_MODEL="gpt-3.5-turbo"  # or your preferred model
   export LLM_API_KEY="your-api-key"  # or OPENAI_API_KEY
   export LLM_BASE_URL="your-base-url"  # optional, for custom endpoints
   ```

**Note**: This lab is validated for LangChain 1.2+. Examples use modern patterns including LCEL (LangChain Expression Language) where applicable.

## Topics Covered

1. **ConversationBufferMemory**
   - Storing complete conversation history
   - Simple memory for short conversations

2. **ConversationBufferWindowMemory**
   - Sliding window of recent messages
   - Managing memory size for long conversations

3. **ConversationSummaryMemory**
   - Summarizing old messages
   - Maintaining context without storing full history

4. **ConversationSummaryBufferMemory**
   - Combining summary and recent messages
   - Optimal balance for long conversations

5. **Vector Store Memory**
   - Semantic search over conversation history
   - Advanced memory retrieval

6. **Memory in Chains and Agents**
   - Integrating memory with chains using LCEL
   - Using memory with ConversationChain
   - Manual memory management in custom chains

## Exercises

1. **Exercise 1**: Build a chatbot with conversation history
2. **Exercise 2**: Implement sliding window memory for recent context
3. **Exercise 3**: Create a memory system that summarizes old conversations
4. **Exercise 4**: Build a customer support assistant with context retention

## Examples

- `01_buffer_memory.py` - Basic conversation buffer
- `02_window_memory.py` - Sliding window memory
- `03_summary_memory.py` - Summary-based memory
- `04_summary_buffer_memory.py` - Combined summary and buffer
- `05_memory_in_chain.py` - Using memory with chains

## Key Concepts

### Buffer Memory

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, {"output": "Hello!"})
```

### Window Memory

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=3)  # Keep last 3 exchanges
```

### Summary Memory

```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(llm=llm)
```

### Memory with LCEL (LangChain Expression Language)

```python
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
memory = ConversationBufferMemory(return_messages=True)
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])
chain = prompt | llm

# Use memory manually
memory_variables = memory.load_memory_variables({})
response = chain.invoke({
    "input": "Hello",
    "chat_history": memory_variables["chat_history"]
})
memory.save_context({"input": "Hello"}, {"output": response.content})
```

## Next Steps

After completing this lab, proceed to [Lab 3: Agents and Tools](../lab-03-agents/README.md).

