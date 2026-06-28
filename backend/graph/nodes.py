from agents.conversation_agent import run_conversation_agent
from agents.image_agent import run_image_agent
from agents.history_agent import run_history_agent
from agents.evidence_agent import run_evidence_agent
from agents.decision_agent import run_decision_agent


# ---------------- Conversation ----------------

def conversation_node(state):

    result = run_conversation_agent(
        state["conversation"]
    )

    state["conversation_result"] = result

    return state


# ---------------- Image ----------------

def image_node(state):

    result = run_image_agent(
        state["image_paths"]
    )

    state["image_result"] = result

    return state


# ---------------- History ----------------

def history_node(state):

    result = run_history_agent(
        state["user_id"]
    )

    state["history_result"] = result

    return state


# ---------------- Evidence ----------------

def evidence_node(state):

    result = run_evidence_agent(

        state["conversation_result"],

        state["image_result"]

    )

    state["evidence_result"] = result

    return state


# ---------------- Decision ----------------

def decision_node(state):

    result = run_decision_agent(

        state["conversation_result"],

        state["image_result"],

        state["history_result"],

        state["evidence_result"]

    )

    state["decision_result"] = result

    return state