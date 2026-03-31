from fastapi import APIRouter, Depends, HTTPException, Query, Path, status
from app.schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    StudentListResponse,
    MessageResponse,
)
from app.database import students_db
import app.database as db_module
from app.dependencies import verify_api_key

router = APIRouter()

@router.get("/", response_model=StudentListResponse)
def list_students(
    department: str | None = Query(default=None, description="Filter by department"),
    min_age: int | None = Query(default=None, ge=5, le=100, description="Minimum age"),
):
    students = list(students_db.values())

    if department:
        students = [
            student for student in students
            if student["department"].lower() == department.lower()
        ]

    if min_age is not None:
        students = [
            student for student in students
            if student["age"] >= min_age
        ]

    return {
        "total": len(students),
        "students": students,
    }


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int = Path(..., ge=1, description="Student ID")
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return student


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def create_student(payload: StudentCreate):
    # Check duplicate email
    for student in students_db.values():
        if student["email"].lower() == payload.email.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

    new_student = {
        "id": db_module.next_student_id,
        **payload.model_dump(),
    }
    students_db[db_module.next_student_id] = new_student
    db_module.next_student_id += 1
    return new_student


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    dependencies=[Depends(verify_api_key)],
)
def update_student(
    payload: StudentUpdate,
    student_id: int = Path(..., ge=1, description="Student ID"),
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    update_data = payload.model_dump(exclude_unset=True)

    if "email" in update_data:
        for existing_id, existing_student in students_db.items():
            if (
                existing_id != student_id
                and existing_student["email"].lower() == update_data["email"].lower()
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists",
                )

    student.update(update_data)
    students_db[student_id] = student
    return student


@router.delete(
    "/{student_id}",
    response_model=MessageResponse,
    dependencies=[Depends(verify_api_key)],
)
def delete_student(
    student_id: int = Path(..., ge=1, description="Student ID")
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    del students_db[student_id]
    return {
        "success": True,
        "message": f"Student with ID {student_id} deleted successfully",
    }