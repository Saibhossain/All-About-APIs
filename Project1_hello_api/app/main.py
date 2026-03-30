from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="Project 1 - Hello API",
    description="A beginner Fast API to understand API basics",
    version="1.0.0"
)
app.include_router(router)