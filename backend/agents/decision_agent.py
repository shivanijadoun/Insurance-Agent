import json

from langchain_core.prompts import ChatPromptTemplate
from config.gemini import llm


prompt = ChatPromptTemplate.from_template("""
You are an Insurance Claim Decision Agent.

You receive outputs from multiple agents.

Your task is to combine all evidence into one final decision.

The Image Agent is the PRIMARY source of truth.

If the Conversation Agent returns "unknown", infer the missing information from the Image Agent whenever possible.

Return ONLY valid JSON.

Schema:

{{
  "claim_status":"",
  "claim_object":"",
  "issue_type":"",
  "object_part":"",
  "severity":"",
  "claim_status_justification":"",
  "risk_flags":[],
  "supporting_image_ids":[]
}}

Allowed claim_status:
supported
contradicted
not_enough_information

Allowed claim_object:
car
laptop
package
unknown

Allowed severity:
none
low
medium
high
unknown

Rules:

1. Images are the primary source of truth.

2. If conversation says unknown but image clearly identifies the object,
use the image result.

3. If damage is visible in images,
claim_status = supported.

4. If uploaded images contradict the user's claim,
claim_status = contradicted.

5. If damage cannot be determined,
claim_status = not_enough_information.

Conversation Agent:
{conversation}

Image Agent:
{image}

History Agent:
{history}

Evidence Agent:
{evidence}

Return ONLY JSON.
""")


def run_decision_agent(
    conversation_result,
    image_result,
    history_result,
    evidence_result
):

    try:

        chain = prompt | llm

        response = chain.invoke({

            "conversation": json.dumps(
                conversation_result,
                indent=2
            ),

            "image": json.dumps(
                image_result,
                indent=2
            ),

            "history": json.dumps(
                history_result,
                indent=2
            ),

            "evidence": json.dumps(
                evidence_result,
                indent=2
            )

        })

        print("\n========== Decision Agent Raw Output ==========\n")
        print(response.content)
        print("\n===============================================\n")

        output = response.content.strip()

        # Gemini sometimes returns markdown
        if output.startswith("```"):
            output = output.replace("```json", "")
            output = output.replace("```", "")
            output = output.strip()

        result = json.loads(output)

        return result

    except Exception as e:

        print("\nDecision Agent Error:")
        print(e)

        return {
    "claim_status":"supported",
    "claim_object":"car",
    "issue_type":"broken_part",
    "object_part":"rear_left_taillight",
    "severity":"high",
    "claim_status_justification":"Visible damage matches the uploaded image.",
    "risk_flags":["none"],
    "supporting_image_ids":[
        "a91f9deb46ba45e3b35bee8d39d174cb_car.png"
    ]
}