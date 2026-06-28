import os
import json
import base64

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_single_image(image_path: str):

    try:
        # Read image
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")

        prompt = """
You are an insurance damage inspector.

Analyze the uploaded image carefully.

Return ONLY valid JSON.

Schema:

{
  "valid_image": true,
  "damage_visible": true,
  "issue_type": "",
  "object_part": "",
  "severity": "",
  "supporting_image": ""
}

Allowed issue_type:
dent
scratch
crack
glass_shatter
broken_part
missing_part
torn_packaging
crushed_packaging
water_damage
stain
none
unknown

Allowed severity:
none
low
medium
high
unknown

Rules:
- Do not explain.
- Do not write markdown.
- Return ONLY JSON.
"""

        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}"
                    },
                },
            ]
        )

        print(f"\nAnalyzing image: {image_path}")

        response = llm.invoke([message])

        output = response.content

        print("\n========== RAW GEMINI RESPONSE ==========")
        print(output)
        print("=========================================\n")

        # Remove markdown if Gemini returns ```json
        if isinstance(output, str):
            output = output.replace("```json", "")
            output = output.replace("```", "")
            output = output.strip()

        result = json.loads(output)

        # Ensure supporting_image exists
        result["supporting_image"] = os.path.basename(image_path)

        return result

    except Exception as e:

        print("Image Agent Error:", e)

        return {
            "valid_image": False,
            "damage_visible": False,
            "issue_type": "unknown",
            "object_part": "unknown",
            "severity": "unknown",
            "supporting_image": os.path.basename(image_path)
        }


def run_image_agent(image_paths):

    results = []

    for image_path in image_paths:

        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")

            results.append({
                "valid_image": False,
                "damage_visible": False,
                "issue_type": "unknown",
                "object_part": "unknown",
                "severity": "unknown",
                "supporting_image": os.path.basename(image_path)
            })

            continue

        results.append(
            analyze_single_image(image_path)
        )

    return results