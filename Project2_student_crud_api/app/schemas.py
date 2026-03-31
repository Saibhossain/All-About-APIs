from typing_extensions import Self

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any


class StudentBase(BaseModel):
    name :str = Field(..., min_length=2, max_length=50, description="Student full name")
    age :int = Field(...,ge=5, le=100, description="Student age")
    department : str= Field(..., min_length=2, max_length=200, description="Department name please")
    email: str= Field(..., min_length=5,max_length=100,description="Provide Student email")

    @field_validator("name")
    @classmethod
    def validate_name (cls, value: str) -> str:
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters and space")
        return value.title()


class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=50)
    age: Optional[int] = Field(default=None, ge=5, le=100)
    department: Optional[str] = Field(default=None, min_length=2, max_length=50)
    email: Optional[str] = Field(default=None, min_length=5, max_length=100)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters and spaces")
        return value.title()

class StudentResponse(StudentBase):
    id: int


class StudentListResponse(BaseModel):
    total: int
    students: list[StudentResponse]


class MessageResponse(BaseModel):
    success: bool
    message: str