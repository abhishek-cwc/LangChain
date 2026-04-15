from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class Student(BaseModel):
    name: str = 'abhishek'
    age: int | None = None
    cgpa: float = Field(gt=0, lt=10, description="cgpa lies bw 0 to 10", default=5)
    result: Literal["Pass", "Fail"]
    email: EmailStr


st_data = {
    "age": "20",
    "cgpa": 8.5,
    "result": "Pass",
    "email": "test@example.com"
}

student = Student(**st_data)

print(student.age)
print(student.cgpa)
print(student.email)

print(dict(student))
print(student.model_dump_json())