# Project 2 - student CRUD api

go to project folder 

    cd Project2_student_crud_api

## Run
```bash
uvicorn app.main:app --reload
```

Open
    
    API: http://127.0.0.1:8000
    Docs: http://127.0.0.1:8000/docs

## Test endpoints
Root

    GET /
List all students

    GET /students

Filter by department

    GET /students?department=Computer Science

Filter by minimum age

    GET /students?min_age=22

Get one student

    GET /students/1

Create student

    POST /students
    x-api-key: student-secret-key

Body:
```json
{
  "name": "Sara Ali",
  "age": 24,
  "department": "Mathematics",
  "email": "sara@example.com"
}
```
Update student

    PUT /students/1
    x-api-key: student-secret-key

Body:
```json
{
  "age": 22,
  "department": "Software Engineering"
}
```

Delete student
    
    DELETE /students/2
    x-api-key: student-secret-key


## What this project teaches

This project uses the main FastAPI building blocks:

* FastAPI() for creating the app
* APIRouter() for grouping routes
* decorators like @router.get() and @router.post()
* BaseModel for validation
* Query(), Path(), and Header() for request data
* HTTPException for clean API errors
* status constants instead of hard-coded numbers
* Depends() for reusable logic like auth checks