from fastapi import APIRouter, Depends
import app.database as db_module
from app.database import prediction_history_db
from app.dependencies import get_current_user
from app.schemas import (
    RiskPredictRequest,
    RiskPredictResponse,
    RiskExplainResponse,
    PredictionHistoryResponse,
)
from app.services.predictor import (
    calculate_risk_score,
    get_risk_level,
    generate_explanation,
    generate_recommendations,
)

router = APIRouter()


@router.post("/risk", response_model=RiskPredictResponse)
def predict_risk(
    payload: RiskPredictRequest,
    current_user: dict = Depends(get_current_user),
):
    score = calculate_risk_score(payload)
    level = get_risk_level(score)

    prediction_record = {
        "id": db_module.next_prediction_id,
        "user_id": current_user["id"],
        "risk_score": score,
        "risk_level": level,
        "input_data": payload.model_dump(),
    }

    prediction_history_db.append(prediction_record)
    db_module.next_prediction_id += 1

    return {
        "risk_score": score,
        "risk_level": level,
    }


@router.post("/explain", response_model=RiskExplainResponse)
def explain_prediction(
    payload: RiskPredictRequest,
    current_user: dict = Depends(get_current_user),
):
    score = calculate_risk_score(payload)
    level = get_risk_level(score)
    explanation = generate_explanation(payload, score, level)
    recommendations = generate_recommendations(level)

    prediction_record = {
        "id": db_module.next_prediction_id,
        "user_id": current_user["id"],
        "risk_score": score,
        "risk_level": level,
        "input_data": payload.model_dump(),
    }

    prediction_history_db.append(prediction_record)
    db_module.next_prediction_id += 1

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": explanation,
        "recommendations": recommendations,
    }


@router.get("/history", response_model=PredictionHistoryResponse)
def get_prediction_history(current_user: dict = Depends(get_current_user)):
    user_history = [
        item for item in prediction_history_db
        if item["user_id"] == current_user["id"]
    ]

    return {
        "total": len(user_history),
        "history": user_history,
    }