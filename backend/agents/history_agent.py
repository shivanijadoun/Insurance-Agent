import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "dataset", "user_history.csv")


def safe_int(value):
    try:
        return int(value)
    except:
        return 0


def create_history_file():
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    df = pd.DataFrame(columns=[
        "user_id",
        "past_claim_count",
        "accept_claim",
        "manual_review_claim",
        "rejected_claim",
        "last_90_days_claim_count",
        "history_flags",
        "history_summary"
    ])

    df.to_csv(HISTORY_FILE, index=False)

    return df


def run_history_agent(user_id):

    # Create CSV if it doesn't exist
    if not os.path.exists(HISTORY_FILE):
        df = create_history_file()
    else:
        df = pd.read_csv(HISTORY_FILE)

    # New user
    if user_id not in df["user_id"].values:

        new_user = {
            "user_id": user_id,
            "past_claim_count": 0,
            "accept_claim": 0,
            "manual_review_claim": 0,
            "rejected_claim": 0,
            "last_90_days_claim_count": 0,
            "history_flags": "",
            "history_summary": "New customer"
        }

        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_csv(HISTORY_FILE, index=False)

        return {
            "history_found": False,
            "history_created": True,
            "past_claim_count": 0,
            "accepted_claims": 0,
            "manual_review_claims": 0,
            "rejected_claims": 0,
            "last_90_days_claim_count": 0,
            "risk_flags": ["none"],
            "history_summary": "New customer profile created."
        }

    # Existing user
    user = df[df["user_id"] == user_id].iloc[0]

    past_claim_count = safe_int(user["past_claim_count"])
    accepted_claims = safe_int(user["accept_claim"])
    manual_review_claims = safe_int(user["manual_review_claim"])
    rejected_claims = safe_int(user["rejected_claim"])
    last_90_days = safe_int(user["last_90_days_claim_count"])

    risk_flags = []

    if last_90_days >= 5:
        risk_flags.append("user_history_risk")

    if rejected_claims >= 3:
        risk_flags.append("manual_review_required")

    history_flags = str(user["history_flags"])

    if history_flags:
        for flag in history_flags.split(";"):
            flag = flag.strip()
            if flag:
                risk_flags.append(flag)

    if not risk_flags:
        risk_flags.append("none")

    return {
        "history_found": True,
        "history_created": False,
        "past_claim_count": past_claim_count,
        "accepted_claims": accepted_claims,
        "manual_review_claims": manual_review_claims,
        "rejected_claims": rejected_claims,
        "last_90_days_claim_count": last_90_days,
        "risk_flags": list(set(risk_flags)),
        "history_summary": user["history_summary"]
    }