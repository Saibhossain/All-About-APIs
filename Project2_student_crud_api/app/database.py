from typing import Dict

# this is a Fake Database

students_db: Dict[int, dict]= {
    1:{
        "id": 1,
        "name": "Amina Rahman",
        "age": 32,
        "department":"Computer Science",
        "email": "amina@gmail.com",
    },
    2:{
        "id": 2,
        "name": "jamila Rahman",
        "age": 23,
        "department": "Computer Science",
        "email": "jamila@gmail.com",
    },
    3: {
        "id": 3,
        "name": "Karim Hasan",
        "age": 23,
        "department": "Electrical Engineering",
        "email": "karim@gmail.com",
    },
}
next_student_id = 4