import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    """Initialize and return the Google GenAI model."""
    
    return ChatGoogleGenerativeAI(
        project=os.getenv("GCP_PROJECT"),
        location=os.getenv("GCP_LOCATION"),
        model="gemini-2.0-flash-lite-001",
        temperature=0
    )