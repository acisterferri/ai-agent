# Importing necessary types from the typing module
from typing import TypedDict, List  

# Define a TypedDict named 'State' to represent a structured dictionary
class State(TypedDict):

    url: str # Stores the URL from Medium
    text: str  # Stores the original input text
    classification: str  # Represents the classification result (e.g., category label)
    entities: List[str]  # Holds a list of extracted entities (e.g., named entities)
    summary: str  # Stores a summarized version of the text
    success: bool # Success of the Agent when calling the article