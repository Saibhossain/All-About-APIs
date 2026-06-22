from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Literal


class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    role: Literal["user", "admin"] = "user"

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters and spaces")
        return value.title()


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"