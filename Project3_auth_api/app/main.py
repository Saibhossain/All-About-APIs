from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router

app = FastAPI(
    title="Project 3 - Auth API",
    description="Authentication API with FastAPI, password hashing, and JWT",
    version="1.0.0",
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {
        "message": "Welcome to Project 3 - Auth API",
        "docs": "/docs",
    }