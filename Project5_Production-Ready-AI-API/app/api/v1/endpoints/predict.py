from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.prediction import (
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    score = calculate_risk_score(payload)
    level = get_risk_level(score)

    prediction = Prediction(
        user_id=current_user.id,
        risk_score=score,
        risk_level=level,
        input_data=payload.model_dump(),
    )
    db.add(prediction)
    db.commit()

    return {
        "risk_score": score,
        "risk_level": level,
    }


@router.post("/explain", response_model=RiskExplainResponse)
def explain_prediction(
    payload: RiskPredictRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    score = calculate_risk_score(payload)
    level = get_risk_level(score)
    explanation = generate_explanation(payload, score, level)
    recommendations = generate_recommendations(level)

    prediction = Prediction(
        user_id=current_user.id,
        risk_score=score,
        risk_level=level,
        input_data=payload.model_dump(),
    )
    db.add(prediction)
    db.commit()

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": explanation,
        "recommendations": recommendations,
    }


@router.get("/history", response_model=PredictionHistoryResponse)
def get_prediction_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    history = (
        db.query(Prediction)
        .filter(Prediction.user_id == current_user.id)
        .order_by(Prediction.id.desc())
        .all()
    )

    return {
        "total": len(history),
        "history": history,
    }