from fastapi import APIRouter, Header, HTTPException
from app.schemas import MessageRequest, MessageResponse

router = APIRouter()

DEMO_API_KEY = "my-secret-key"

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

@router.get("/protected")
def protected_route(x_api_key: str = Header(None)):
    if x_api_key != DEMO_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    return {
        "success": True,
        "message": "You accessed a protected endpoint"
    }