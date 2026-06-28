# from fastapi import APIRouter, UploadFile, File, Form
# from typing import List
# import os
# import shutil
# from uuid import uuid4

# from agents.conversation_agent import run_conversation_agent
# from agents.image_agent import run_image_agent
# from agents.history_agent import run_history_agent
# from agents.evidence_agent import run_evidence_agent
# from agents.decision_agent import run_decision_agent

# router = APIRouter()

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @router.post("/upload")
# async def upload(
#     user_id: str = Form(...),
#     message: str = Form(...),
#     images: List[UploadFile] = File(...)
# ):
#     image_paths = []

#     for image in images:
#         filename = f"{uuid4().hex}_{image.filename}"
#         path = os.path.join(UPLOAD_FOLDER, filename)

#         with open(path, "wb") as buffer:
#             shutil.copyfileobj(image.file, buffer)

#         image_paths.append(path)

#     conversation = run_conversation_agent(message)
#     image = run_image_agent(image_paths)
#     history = run_history_agent(user_id)
#     evidence = run_evidence_agent(conversation, image)

#     final = run_decision_agent(
#         conversation,
#         image,
#         history,
#         evidence
#     )

#     return {
#         "conversation": conversation,
#         "image": image,
#         "history": history,
#         "evidence": evidence,
#         "final": final
#     }

from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import os
import shutil
from uuid import uuid4
import traceback

from agents.conversation_agent import run_conversation_agent
from agents.image_agent import run_image_agent
from agents.history_agent import run_history_agent
from agents.evidence_agent import run_evidence_agent
from agents.decision_agent import run_decision_agent

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload(
    user_id: str = Form(...),
    message: str = Form(...),
    images: List[UploadFile] = File(...)
):
    try:

        image_paths = []

        for image in images:
            filename = f"{uuid4().hex}_{image.filename}"
            path = os.path.join(UPLOAD_FOLDER, filename)

            with open(path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            image_paths.append(path)

        print("\n===== Conversation Agent =====")
        conversation = run_conversation_agent(message)
        print(conversation)

        print("\n===== Image Agent =====")
        image = run_image_agent(image_paths)
        print(image)

        print("\n===== History Agent =====")
        history = run_history_agent(user_id)
        print(history)

        print("\n===== Evidence Agent =====")
        evidence = run_evidence_agent(conversation, image)
        print(evidence)

        print("\n===== Decision Agent =====")
        final = run_decision_agent(
            conversation,
            image,
            history,
            evidence
        )
        print(final)

        return {
            "conversation": conversation,
            "image": image,
            "history": history,
            "evidence": evidence,
            "final": final
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }