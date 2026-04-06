# Project 4 - AI Inference API

## Run
```bash
uvicorn app.main:app --reload
```

Docs

    http://127.0.0.1:8000/docs

Flow
Register a user
Login to get JWT token
Authorize in Swagger docs
Call prediction endpoints
Endpoints
POST /auth/register
POST /auth/login
GET /users/me
GET /users/admin-only
POST /predict/risk
POST /predict/explain
GET /predict/history


