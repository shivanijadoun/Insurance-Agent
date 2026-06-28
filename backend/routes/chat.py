from fastapi import APIRouter
from pydantic import BaseModel

from agents.conversation_agent import run_conversation_agent
from agents.image_agent import run_image_agent
from agents.history_agent import run_history_agent
from agents.evidence_agent import run_evidence_agent
from agents.decision_agent import run_decision_agent

router = APIRouter()


class ChatRequest(BaseModel):
    user_id: str
    message: str
    image_paths: list[str] = []


@router.post("/chat")
def chat_endpoint(req: ChatRequest):

    try:
        print("\n===== Conversation Agent =====")
        conversation_result = run_conversation_agent(req.message)
        print(conversation_result)

        print("\n===== Image Agent =====")
        image_result = run_image_agent(req.image_paths) if req.image_paths else []
        print(image_result)

        print("\n===== History Agent =====")
        history_result = run_history_agent(req.user_id)
        print(history_result)

        print("\n===== Evidence Agent =====")
        evidence_result = run_evidence_agent(
            conversation_result,
            image_result
        )
        print(evidence_result)

        print("\n===== Decision Agent =====")
        final_result = run_decision_agent(
            conversation_result,
            image_result,
            history_result,
            evidence_result
        )
        print(final_result)

        return {
            "conversation": conversation_result,
            "image": image_result,
            "history": history_result,
            "evidence": evidence_result,
            "final": final_result
        }

    except Exception as e:
        import traceback
        traceback.print_exc()

        return {
            "error": str(e)
        }