from tkinter import BooleanVar

from pydantic import BaseModel, Field

class MessageRequest(BaseModel):
    name : str = Field(...,min_length=2, max_length=50, description="User name")
    message: str= Field(..., min_length=1, max_length=200,description="A short message")

class MessageResponse(BaseModel):
    success : bool
    reply:str