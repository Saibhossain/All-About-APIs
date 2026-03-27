from pydantic import BaseModel, EmailStr, AnyUrl


class Patient(BaseModel):
    name : str
    email: EmailStr
    age: int

def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print('inserted')


patient_info = {'name':'nitish','email':'saib@gmail.com','age':'30'}

patient1 = Patient(**patient_info)

insert_patient_date(patient1)