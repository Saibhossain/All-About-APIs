from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.database import users_db
from app.security import decode_access_token
from app.schemas import TokenData
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    for user in users_db.values():
        if user["email"]== token_data.email:
            return user

    raise credentials_exception

def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user["role"]!= "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Admin access required",
        )
    return current_user
