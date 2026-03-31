from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal

class UserRegister(BaseModel):
    name : str = Field(..., min_length=4,max_length=120,description="Full name please")
    email: EmailStr
    password:str =Field(..., min_length=6,max_length=100, description="plain password not any change or use +-@# signe")
    role: Literal["user","admin"] = "user"

    @field_validator("name")
    @classmethod
    def validate_name(cls,value:str) -> str:
        if not value.replace(" ","").isalpha():
            raise ValueError("Error should contain only letters and spaces")
        return value.title()