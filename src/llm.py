import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    """Initialize and return the Google GenAI model."""

    # Load environment variables
    load_dotenv()
    
    return ChatGoogleGenerativeAI(
        project=os.getenv("GCP_PROJECT"),
        location=os.getenv("GCP_LOCATION"),
        model="gemini-2.0-flash-lite-001",
        temperature=0
    )