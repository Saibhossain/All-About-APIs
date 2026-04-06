from datetime import timedelta
from fastapi import APIRouter, HTTPException, status

from app.schemas import UserRegister, UserLogin, UserResponse, TokenResponse
from app.database import users_db
import app.database as db_module
from app.security import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserRegister):
    for user in users_db.values():
        if user["email"].lower() == payload.email.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

    hashed_password = hash_password(payload.password)

    new_user = {
        "id": db_module.next_user_id,
        "name": payload.name,
        "email": payload.email,
        "hashed_password": hashed_password,
        "role": payload.role,
    }

    users_db[db_module.next_user_id] = new_user
    db_module.next_user_id += 1

    return {
        "id": new_user["id"],
        "name": new_user["name"],
        "email": new_user["email"],
        "role": new_user["role"],
    }


@router.post("/login", response_model=TokenResponse)
def login_user(payload: UserLogin):
    user = None

    for existing_user in users_db.values():
        if existing_user["email"].lower() == payload.email.lower():
            user = existing_user
            break

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={"sub": user["email"], "role": user["role"]},
        expires_delta=timedelta(minutes=60),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }