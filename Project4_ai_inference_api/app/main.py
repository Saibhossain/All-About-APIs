from fastapi import FastAPI

app = FastAPI(
    title="Project 4 - AI Inference API",
    description="AI inference API with JWT authentication and prediction history",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Project 4 - AI Inference API",
        "docs": "/docs",
    }