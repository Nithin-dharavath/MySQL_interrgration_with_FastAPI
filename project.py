from docutils.nodes import author
from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import session
import model
from schema.user_input import StudentCreate

app = FastAPI()


@app.post("/create")
def create_student(student: StudentCreate, db: session = Depends(get_db)):
    db_student = model.book(rollno = student.rollno, fullname = student.fullname, age = student.age, college = student.college, branch = student.college)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

