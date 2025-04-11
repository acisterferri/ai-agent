from langgraph.graph import StateGraph, END
from .nodes import extract_text_from_url_node, decision_node, classification_node, entity_extraction_node, summarize_node
from .state import State

def create_workflow() -> StateGraph:
    workflow = StateGraph(State)

    # Add nodes
    workflow.add_node("extract_text_from_url", extract_text_from_url_node)
    workflow.add_node("classification_node", classification_node)
    workflow.add_node("entity_extraction", entity_extraction_node)
    workflow.add_node("summarization", summarize_node)

    # Set the entry point of the graph
    workflow.set_entry_point("extract_text_from_url")

    # Add edges to the graph
    workflow.add_conditional_edges("extract_text_from_url", decision_node, {"continue": "classification_node", "end": END})
    workflow.add_edge("classification_node", "entity_extraction")
    workflow.add_edge("entity_extraction", "summarization")
    workflow.add_edge("summarization", END)

    return workflow.compile()