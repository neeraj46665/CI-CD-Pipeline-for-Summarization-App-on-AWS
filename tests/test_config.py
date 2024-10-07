import os
import pytest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_environment_variables():
    """Test if environment variables are set correctly."""
    assert os.getenv("COHERE_API_KEY") is not None, "COHERE_API_KEY should be set"
    assert os.getenv("GROQ_API_KEY") is not None, "GROQ_API_KEY should be set"

def test_api_key_format():
    """Test if API keys have the correct format."""
    cohere_api_key = os.getenv("COHERE_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")

    assert len(cohere_api_key) == 40, "COHERE_API_KEY should be 40 characters long"
    assert len(groq_api_key) > 0, "GROQ_API_KEY should not be empty"

# Add any additional configuration-related tests here
