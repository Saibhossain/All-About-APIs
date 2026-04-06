from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal


# =========================
# AUTH SCHEMAS
# =========================
class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100, description="Plain password")
    role: Literal["user", "admin"] = "user"

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters and spaces")
        return value.title()


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class MessageResponse(BaseModel):
    success: bool
    message: str


# =========================
# PREDICTION SCHEMAS
# =========================
class RiskPredictRequest(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Patient age")
    smoking: bool = Field(..., description="Whether patient is a smoker")
    coughing: bool = Field(..., description="Whether patient has persistent coughing")
    chest_pain: bool = Field(..., description="Whether patient has chest pain")
    fatigue: bool = Field(..., description="Whether patient has fatigue")
    family_history: bool = Field(..., description="Whether family has cancer history")

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Age must be greater than zero")
        return value


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


class PredictionHistoryResponse(BaseModel):
    total: int
    history: list[PredictionHistoryItem]