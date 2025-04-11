# AI Agent with Gemini and Langchain

This repository demonstrates the creation of an AI agent using Google Gemini and Langchain. The agent is designed to extract text from Medium articles, classify the content, extract entities, and summarize the text.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [llm.py](#llmpy)
  - [nodes.py](#nodespy)
  - [state.py](#statepy)
  - [utils.py](#utilspy)
  - [workflow.py](#workflowpy)
  - [agent.py](#agentpy)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases how to build an AI agent that interacts with web content using Google Gemini for language processing and Langchain for workflow management. The agent can analyze articles, classify them, extract named entities, and provide summaries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Agent.git
   cd AI-Agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google Cloud project and Secret Manager to access the necessary API keys.

## Usage

To run the agent, execute the following command:
```bash
python agent.py
```
You will be prompted to enter a Medium article URL for analysis.

## Code Overview

### llm.py

This module initializes the Google Gemini model.

```python
def get_llm():
    """Initialize and return the Google GenAI model."""
    return ChatGoogleGenerativeAI(
        project=os.getenv("GCP_PROJECT"),
        location=os.getenv("GCP_LOCATION"),
        model="gemini-2.0-flash-lite-001",
        temperature=0
    )
```

### nodes.py

This module contains various nodes for the workflow, including text extraction, decision-making, classification, entity extraction, and summarization.

- extract_text_from_url_node: Extracts text from a given Medium article URL.
- decision_node: Decides whether to continue the workflow based on extraction success.
- classification_node: Classifies the extracted text into predefined categories.
- entity_extraction_node: Extracts named entities from the text.
- summarize_node: Summarizes the text into a single sentence.

### state.py

Defines a structured dictionary using TypedDict to represent the state of the agent.

```python
class State(TypedDict):
    url: str
    text: str
    classification: str
    entities: List[str]
    summary: str
    success: bool
```

### utils.py

Contains utility functions, including accessing secrets from Google Cloud Secret Manager.

```python
def access_secret_version():
    # Access the latest version of the secret
    ...
```

### workflow.py

Creates a state graph for the workflow, connecting the various nodes defined in nodes.py.

```python
def create_workflow() -> StateGraph:
    workflow = StateGraph(State)
    ...
    return workflow.compile()
```

### agent.py

The main entry point of the application. It loads environment variables, initializes the workflow, and processes the user input.

```python
def main():
    ...
    result = app.invoke(state_input)
    ...
```

## Examples

1. Extracting Text: Input a Medium article URL to extract its content.
2. Classification: The agent will classify the content into categories like News, Blog, Research, or Other.
3. Entity Extraction: Named entities such as persons, organizations, and locations will be extracted.
4. Summarization: A concise summary of the article will be provided.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.