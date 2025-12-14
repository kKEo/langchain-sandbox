"""
Verify that your LangChain environment is set up correctly.
Run this script to check your installation and API keys.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def verify_setup():
    """Verify LangChain setup and API keys."""
    print("🔍 Verifying LangChain setup...\n")
    
    # Check Python version
    import sys
    python_version = sys.version_info
    print(f"✓ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    # Check LangChain installation
    try:
        import langchain
        print(f"✓ LangChain version: {langchain.__version__}")
    except ImportError:
        print("❌ LangChain not installed. Run: pip install -r requirements.txt")
        return False
    
    # Check API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if openai_key:
        print(f"✓ OpenAI API key found: {openai_key[:10]}...")
    else:
        print("⚠️  OpenAI API key not found (set OPENAI_API_KEY)")
    
    if anthropic_key:
        print(f"✓ Anthropic API key found: {anthropic_key[:10]}...")
    else:
        print("⚠️  Anthropic API key not found (optional, set ANTHROPIC_API_KEY)")
    
    if not openai_key and not anthropic_key:
        print("\n❌ At least one API key is required (OpenAI or Anthropic)")
        return False
    
    # Test basic import
    try:
        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import PromptTemplate
        print("✓ Core LangChain modules imported successfully")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    print("\n✅ Setup verification complete! You're ready to start Lab 1.")
    return True

if __name__ == "__main__":
    verify_setup()

