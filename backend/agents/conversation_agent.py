import json
from langchain_core.prompts import ChatPromptTemplate
from config.gemini import llm


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an insurance claim extraction agent.

Extract structured information from the user conversation.

Return ONLY valid JSON.

{{
  "claim_object": "car | laptop | package | unknown",
  "issue_type": "dent | scratch | crack | glass_shatter | broken_part | missing_part | torn_packaging | crushed_packaging | water_damage | stain | none | unknown",
  "object_part": "",
  "claim_summary": ""
}}

Rules:
- Return ONLY JSON
- No explanation
- If unknown, use "unknown"
"""
    ),
    ("human", "{conversation}")
])
def run_conversation_agent(conversation: str):
    chain = prompt | llm

    print("\n===== Conversation Agent (Gemini) =====")

    response = chain.invoke({
        "conversation": conversation
    })

    raw = response.content

    print(raw)

    try:
        return json.loads(raw)

    except Exception:
        return {
            "claim_object": "unknown",
            "issue_type": "unknown",
            "object_part": "unknown",
            "claim_summary": conversation
        }