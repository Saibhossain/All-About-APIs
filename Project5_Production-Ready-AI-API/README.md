# Project 5 - Production Ready AI API

## Features
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Docker & Docker Compose
- Prediction service layer
- Health check
- Tests

## Local run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Docker run
```bash
cp .env.example .env
docker compose up --build
```

## API docs

http://127.0.0.1:8000/docs

### Main endpoints

    POST /api/v1/auth/register
    POST /api/v1/auth/login
    GET /api/v1/users/me
    GET /api/v1/users
    POST /api/v1/predict/risk
    POST /api/v1/predict/explain
    GET /api/v1/predict/history
    GET /api/v1/health


---

# 9) How to run it

## Local

```bash
cd project5_production_ready_api
cp .env.example .env
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload