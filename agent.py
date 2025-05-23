from src.workflow import create_workflow
from dotenv import load_dotenv
import os


def main():
    # Load environment variables
    load_dotenv()
    
    # Define a Medium URL to test our agent
    medium_url = input("What Medium article do you want to analyze?:")
    
    # Create the initial state with the URL
    state_input = {"url": medium_url}

    # Create the workflow
    app = create_workflow()

    # Run the agent's full workflow on the state
    result = app.invoke(state_input)

    # Check if the extraction was successful
    if result.get("success", True):
        # Print each component of the result
        print("Classification:", result["classification"])
        print("\nEntities:", result["entities"])
        print("\nSummary:", result["summary"])
    else:
        print("Failed to extract text from the URL |", result["text"])


if __name__ == "__main__":
    main()