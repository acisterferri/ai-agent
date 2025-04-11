import requests
from bs4 import BeautifulSoup
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from .state import State
from .llm import get_llm

llm = get_llm()

def extract_text_from_url_node(state: State):
    """
    Extract text from a Medium article given its URL.
    
    Parameters:
        state (State): The current state dictionary containing the URL to extract text from.
        
    Returns:
        dict: A dictionary with the following keys:
            - "text": The extracted text from the article or an error message.
            - "success": A boolean indicating whether the extraction was successful.
    """
    url = state["url"]  # Get the URL from the state
    try:
        response = requests.get(url)
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            article = soup.find('article')
            if article:
                extracted_text = article.get_text(separator="\n").strip()
                return {"text": extracted_text, "success": True}
            else:
                return {"text": "Could not find the article on the page.", "success": False}
        else:
            return {"text": f"Error accessing the URL: {response.status_code}", "success": False}
    except Exception as e:
        return {"text": f"Exception, invalid URL: {e}", "success": False}


def decision_node(state: State):
    """
    Decide whether to continue the workflow based on the success of the URL extraction.
    
    Parameters:
        state (State): The current state dictionary containing the success flag.
        
    Returns:
        dict: A dictionary indicating whether to continue or stop the workflow.
    """
    if state.get("success", True):
        return "continue"
    else:
        return "end"

def classification_node(state: State):
   """
   Classify the text into one of predefined categories.
   
   Parameters:
       state (State): The current state dictionary containing the text to classify
       
   Returns:
       dict: A dictionary with the "classification" key containing the category result
       
   Categories:
       - News: Factual reporting of current events
       - Blog: Personal or informal web writing
       - Research: Academic or scientific content
       - Other: Content that doesn't fit the above categories
   """

   # Define a prompt template that asks the model to classify the given text
   prompt = PromptTemplate(
       input_variables=["text"],
       template="Classify the following text into one of the categories: News, Blog, Research, or Other.\n\nText: {text}\n\nCategory:"
   )

   # Format the prompt with the input text from the state
   message = HumanMessage(content=prompt.format(text=state["text"]))

   # Invoke the language model to classify the text based on the prompt
   classification = llm.invoke([message]).content.strip()

   # Return the classification result in a dictionary
   return {"classification": classification}


def entity_extraction_node(state: State):
  # Function to identify and extract named entities from text
  # Organized by category (Person, Organization, Location)
  
  # Create template for entity extraction prompt
  # Specifies what entities to look for and format (comma-separated)
  prompt = PromptTemplate(
      input_variables=["text"],
      template="Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma-separated list.\n\nText: {text}\n\nEntities:"
  )
  
  # Format the prompt with text from state and wrap in HumanMessage
  message = HumanMessage(content=prompt.format(text=state["text"]))
  
  # Send to language model, get response, clean whitespace, split into list
  entities = llm.invoke([message]).content.strip().split(", ")
  
  # Return dictionary with entities list to be merged into agent state
  return {"entities": entities}


def summarize_node(state: State):
    # Create a template for the summarization prompt
    # This tells the model to summarize the input text in one sentence
    summarization_prompt = PromptTemplate.from_template(
        """Summarize the following text in one short sentence.
        
        Text: {text}
        
        Summary:"""
    )
    
    # Create a chain by connecting the prompt template to the language model
    # The "|" operator pipes the output of the prompt into the model
    chain = summarization_prompt | llm
    
    # Execute the chain with the input text from the state dictionary
    # This passes the text to be summarized to the model
    response = chain.invoke({"text": state["text"]})
    
    # Return a dictionary with the summary extracted from the model's response
    # This will be merged into the agent's state
    return {"summary": response.content}