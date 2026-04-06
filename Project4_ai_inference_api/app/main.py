from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.predict import router as predict_router

app = FastAPI(
    title="Project 4 - AI Inference API",
    description="AI inference API with JWT authentication and prediction history",
    version="1.0.4",
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(predict_router, prefix="/predict", tags=["Prediction"])


@app.get("/")
def root():
    return {
        "message": "Welcome to Project 4 - AI Inference API",
        "docs": "/docs",
    }