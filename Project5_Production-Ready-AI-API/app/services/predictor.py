from app.schemas.prediction import RiskPredictRequest


def calculate_risk_score(payload: RiskPredictRequest) -> float:
    score = 0.0

    if payload.age >= 60:
        score += 0.25
    elif payload.age >= 45:
        score += 0.15
    elif payload.age >= 30:
        score += 0.05

    if payload.smoking:
        score += 0.25
    if payload.coughing:
        score += 0.15
    if payload.chest_pain:
        score += 0.15
    if payload.fatigue:
        score += 0.10
    if payload.family_history:
        score += 0.10

    return min(round(score, 2), 1.0)


def get_risk_level(score: float) -> str:
    if score >= 0.70:
        return "high"
    if score >= 0.40:
        return "medium"
    return "low"


def generate_explanation(payload: RiskPredictRequest, score: float, level: str) -> str:
    reasons = []

    if payload.smoking:
        reasons.append("smoking increases the estimated risk")
    if payload.coughing:
        reasons.append("persistent coughing is an important symptom")
    if payload.chest_pain:
        reasons.append("chest pain contributes to concern")
    if payload.fatigue:
        reasons.append("fatigue adds some risk signal")
    if payload.family_history:
        reasons.append("family history contributes to overall risk")
    if payload.age >= 45:
        reasons.append("age adds to the risk profile")

    if not reasons:
        reasons.append("there are currently few strong risk factors in the input")

    return (
        f"The predicted risk level is {level} with a score of {score}. "
        f"This result is based on the following factors: {', '.join(reasons)}."
    )


def generate_recommendations(level: str) -> list[str]:
    if level == "high":
        return [
            "Seek medical consultation as soon as possible.",
            "Consider clinical screening or diagnostic tests.",
            "Do not ignore persistent symptoms.",
        ]
    if level == "medium":
        return [
            "Monitor symptoms closely.",
            "Consider speaking with a doctor if symptoms continue.",
            "Improve lifestyle factors such as smoking cessation.",
        ]
    return [
        "Maintain a healthy lifestyle.",
        "Monitor for any new or worsening symptoms.",
        "Seek clinical advice if symptoms appear later.",
    ]