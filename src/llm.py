import os
from langchain_google_genai import ChatGoogleGenerativeAI
from .utils import access_secret_version


def get_llm():
    """Initialize and return the Google GenAI model."""
    
    return ChatGoogleGenerativeAI(
        project=os.getenv("GCP_PROJECT"),
        location=os.getenv("GCP_LOCATION"),
        google_api_key=access_secret_version(),
        model="gemini-2.0-flash-lite-001",
        temperature=0
    )