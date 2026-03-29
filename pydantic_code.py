from pydantic import BaseModel, EmailStr, AnyUrl
from pydantic import Field

class Patient(BaseModel):
    name : str
    email: EmailStr
    weight : float=Field(gt=0)
    age: int

def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.age)
    print('inserted')


patient_info = {'name':'nitish','email':'saib@gmail.com','weight':'1', 'age':'30'}

patient1 = Patient(**patient_info)

insert_patient_date(patient1)