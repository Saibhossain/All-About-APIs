from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.database import users_db
from app.security import decode_access_token
from app.schemas import TokenData
