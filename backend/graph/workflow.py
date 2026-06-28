from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import ClaimState

from graph.nodes import (
    conversation_node,
    image_node,
    history_node,
    evidence_node,
    decision_node
)


workflow = StateGraph(ClaimState)


workflow.add_node(
    "conversation",
    conversation_node
)

workflow.add_node(
    "image",
    image_node
)

workflow.add_node(
    "history",
    history_node
)

workflow.add_node(
    "evidence",
    evidence_node
)

workflow.add_node(
    "decision",
    decision_node
)


workflow.set_entry_point("conversation")


workflow.add_edge(
    "conversation",
    "image"
)

workflow.add_edge(
    "image",
    "history"
)

workflow.add_edge(
    "history",
    "evidence"
)

workflow.add_edge(
    "evidence",
    "decision"
)

workflow.add_edge(
    "decision",
    END
)


claim_graph = workflow.compile()