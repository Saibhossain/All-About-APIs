from fastapi import APIRouter, Depends
from app.dependencies import get_current_user, require_admin
from app.schemas import UserResponse, MessageResponse

router = APIRouter()


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"],
        "role": current_user["role"],
    }


@router.get("/admin-only", response_model=MessageResponse)
def admin_only_route(current_user: dict = Depends(require_admin)):
    return {
        "success": True,
        "message": f"Welcome admin {current_user['name']}, you can access this route.",
    }