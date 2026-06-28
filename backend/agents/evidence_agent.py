# agents/evidence_agent.py

EVIDENCE_RULES = {

    "car": {

        "scratch": {
            "required_evidence": "At least one clear image showing the scratch."
        },

        "dent": {
            "required_evidence": "Two images from different angles showing the dent."
        },

        "crack": {
            "required_evidence": "One close-up image of the crack."
        },

        "glass_shatter": {
            "required_evidence": "Clear image showing shattered glass."
        },

        "broken_part": {
            "required_evidence": "One close-up and one full vehicle image."
        },

        "missing_part": {
            "required_evidence": "Image clearly showing the missing component."
        }

    },

    "laptop": {

        "crack": {
            "required_evidence": "Front image showing cracked screen."
        },

        "broken_part": {
            "required_evidence": "Image showing the damaged component."
        },

        "water_damage": {
            "required_evidence": "Images clearly showing water damage."
        },

        "stain": {
            "required_evidence": "Clear image of the stain."
        }

    },

    "package": {

        "torn_packaging": {
            "required_evidence": "Image of the torn package."
        },

        "crushed_packaging": {
            "required_evidence": "Images from multiple angles."
        },

        "water_damage": {
            "required_evidence": "Images showing water damage."
        }

    }

}


def run_evidence_agent(conversation_result, image_results):

    claim_object = (
        conversation_result.get("claim_object", "unknown") or "unknown"
    ).lower()

    issue_type = (
        conversation_result.get("issue_type", "unknown") or "unknown"
    ).lower()

    # Look for matching evidence rule
    rule = (
        EVIDENCE_RULES
        .get(claim_object, {})
        .get(issue_type)
    )

    if rule is None:

        return {

            "evidence_standard_met": False,

            "evidence_standard_met_reason":
                "No evidence rule exists for this claim.",

            "required_evidence": "unknown",

            "supporting_image_ids": [],

            "valid_image": False

        }

    supporting_images = []

    for img in image_results:

        if (
            img.get("valid_image") is True
            and img.get("damage_visible") is True
            and (img.get("issue_type", "").lower() == issue_type)
        ):

            supporting_images.append(
                img.get("supporting_image")
            )

    if supporting_images:

        return {

            "evidence_standard_met": True,

            "evidence_standard_met_reason":
                "Uploaded images satisfy the required evidence.",

            "required_evidence":
                rule["required_evidence"],

            "supporting_image_ids":
                supporting_images,

            "valid_image": True

        }

    return {

        "evidence_standard_met": False,

        "evidence_standard_met_reason":
            "Uploaded images do not clearly satisfy the evidence requirement.",

        "required_evidence":
            rule["required_evidence"],

        "supporting_image_ids": [],

        "valid_image": False

    }