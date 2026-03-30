from fastapi import APIRouter
from schemas import MessageRequest, MessageResponse

router = APIRouter()

@router.get("/")
def home():
    return  {
        "message": "welcome to project 1 : Hello Api",
        "docs": "/docs"
    }

@router.get("/hello/{name}")
def say_hello(name: str):
    return {
        "success": True,
        "reply":f"Hello, {name}! your API is working."
    }

@router.post("/echo",response_model=MessageResponse)
def echo_message(payload: MessageRequest):
    return MessageResponse(
        success=True,
        reply=f"Hello {payload.name}, you said: {payload.message} "
    )