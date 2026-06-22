from pydantic import BaseModel, Field


class RiskPredictRequest(BaseModel):
    age: int = Field(..., ge=1, le=120)
    smoking: bool
    coughing: bool
    chest_pain: bool
    fatigue: bool
    family_history: bool


class RiskPredictResponse(BaseModel):
    risk_score: float
    risk_level: str


class RiskExplainResponse(BaseModel):
    risk_score: float
    risk_level: str
    explanation: str
    recommendations: list[str]


class PredictionHistoryItem(BaseModel):
    id: int
    user_id: int
    risk_score: float
    risk_level: str
    input_data: dict

    model_config = {"from_attributes": True}


class PredictionHistoryResponse(BaseModel):
    total: int
    history: list[PredictionHistoryItem]