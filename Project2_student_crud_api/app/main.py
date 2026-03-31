from fastapi import FastAPI
from app.routes.students import router as student_router


app = FastAPI(
    title="Project 2 - Student CRUD API",
    description="A beginner-friendly CRUD API built with FastAPI",
    version="1.0.1",
)

app.include_router(student_router,prefix="/students", tags=["Students"])

@app.get("/")
def root():
    return {
        "massage": "Welcome to Preoject 2 -Student CRUD API",
        "docs": "/docs",
    }