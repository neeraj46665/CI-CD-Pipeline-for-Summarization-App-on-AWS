import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to hold the app configuration."""
    
    # Environment Variables
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")  # Cohere API key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Groq API key

    # Other configurations
    DEBUG = os.getenv("DEBUG", "False") == "True"  # Convert string to boolean
    

   
