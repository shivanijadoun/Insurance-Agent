from typing import TypedDict


class ClaimState(TypedDict):

    user_id: str

    conversation: str

    image_paths: list

    conversation_result: dict

    image_result: list

    history_result: dict

    evidence_result: dict

    decision_result: dict