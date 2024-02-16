from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "class": "year 11"
    }
}

class Student(BaseModel):
    name: str
    age: int
    class_: str

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_: Optional[str] = None

@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: updateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.class_ != None:
        students[student_id].class_ = student.class_
    return


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return