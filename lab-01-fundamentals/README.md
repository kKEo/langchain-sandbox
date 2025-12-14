# Lab 1: LangChain Fundamentals - Prompts, Chains, and LLMs

**Level: Moderate**

## Learning Objectives

By the end of this lab, you will be able to:
- Understand LangChain's core architecture and components
- Create and manage prompt templates
- Build basic chains (LLMChain, SequentialChain)
- Work with different LLM providers (OpenAI, Anthropic, etc.)
- Handle LLM outputs and parsing

## Prerequisites

- Python 3.8+
- OpenAI API key (or Anthropic API key)
- Basic understanding of Python
- Familiarity with environment variables

## Setup

1. Install lab-specific dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   # OR
   export ANTHROPIC_API_KEY="your-key-here"
   ```

3. Verify installation:
   ```bash
   python examples/01_verify_setup.py
   ```

## Topics Covered

1. **LangChain Installation and Setup**
   - Installing LangChain and provider packages
   - Environment variable management

2. **Prompt Templates**
   - `PromptTemplate` for text models
   - `ChatPromptTemplate` for chat models
   - Variable substitution and formatting

3. **LLM Interfaces**
   - `LLM` vs `ChatModel` interfaces
   - Working with OpenAI and Anthropic models
   - Model parameters (temperature, max_tokens, etc.)

4. **Basic Chains**
   - `LLMChain` for simple LLM calls
   - `SimpleSequentialChain` for multi-step workflows
   - `SequentialChain` for complex workflows

5. **Output Parsers**
   - `StrOutputParser` for string outputs
   - `PydanticOutputParser` for structured data
   - Custom output parsing

## Exercises

Work through the exercises in order:

1. **Exercise 1**: Create a simple prompt template for text generation
2. **Exercise 2**: Build a chain that generates and formats product descriptions
3. **Exercise 3**: Implement a multi-step chain (generate → summarize → format)
4. **Exercise 4**: Parse structured outputs using Pydantic models

Each exercise includes:
- Starter code in `exercises/exercise_X.py`
- Instructions in the code comments
- Complete solution in `solutions/exercise_X.py`

## Examples

The `examples/` directory contains reference implementations:
- `01_verify_setup.py` - Verify your environment is set up correctly
- `02_basic_prompt.py` - Basic prompt template usage
- `03_chat_prompt.py` - Chat prompt templates
- `04_simple_chain.py` - Simple LLMChain example
- `05_sequential_chain.py` - Multi-step chain example
- `06_output_parsing.py` - Output parsing examples

## Key Concepts

### Prompt Templates

```python
from langchain.prompts import PromptTemplate

template = "Write a {style} story about {topic}"
prompt = PromptTemplate.from_template(template)
```

### Chains

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(style="funny", topic="robots")
```

### Output Parsers

```python
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class Story(BaseModel):
    title: str
    content: str

parser = PydanticOutputParser(pydantic_object=Story)
```

## Next Steps

After completing this lab, proceed to [Lab 2: Memory and Conversation Management](../lab-02-memory/README.md).

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'langchain'`
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: `AuthenticationError` or API key errors
- **Solution**: Verify your API key is set correctly: `echo $OPENAI_API_KEY`

**Issue**: Rate limit errors
- **Solution**: You may be hitting API rate limits. Wait a moment and try again, or use a model with higher rate limits.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com/)

