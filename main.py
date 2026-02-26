from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from schema.user_input import UserInput, StudentUpdate
from config.utility import load_data, save_data

app = FastAPI()

@app.get("/")
def home():
    return {"meassage" : "data base integration with MySQL using fastapi"}

@app.get("/health")
def health_check():
    return {"status" : "True"}

@app.get("/about")
def about():
    return {"meassage" : "project is about the integartion of student data with MySQl through fastapi"}

@app.get("/view")
def view_students():
    data = load_data()
    return data

@app.get("/student/{rollno}")
def student_id(rollno : int = Path(..., description="enter the roll no of the student u want to view")):
    data = load_data()
    for student in data:
        if student["rollno"] == rollno:
            return student
    
    raise HTTPException(status_code=404, detail="student not found")

@app.get("/sort")
def sorted_student (sort_by : str  = Query(..., description="sort on bias of branch or college"), order : str = Query("asc", description="sort by asc or des order")):
    valid_fields = ["branch", "college"]
    valid_orders = ["asc", "desc"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    if order not in valid_orders:
        raise HTTPException(status_code=400, detail="Invalid order value")

    data = load_data()  # assuming dictionary {rollno: student_dict}
    reverse_sort = order == "desc"
    sorted_data = sorted(
        data,
        key=lambda x: x[sort_by],
        reverse=(order == "desc")
    )

    return sorted_data

@app.post("/create")
def create_student(student : UserInput):
    data = load_data()

    if student in data:
        raise HTTPException(status_code="400", detail="user already exists")
    data.append(student.model_dump())
    save_data(data)
    return JSONResponse(status_code=201, content={"message" : "new student is created in database"})

@app.patch("/edit/{rollno}")
def patch_student(rollno: int, student: StudentUpdate):
    data = load_data()

    for s in data:
        if s["rollno"] == rollno:
            update_data = student.model_dump(exclude_unset=True)
            s.update(update_data)
            save_data(data)
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/delete/{rollno}")
def student_delete(rollno : int):
    data = load_data()

    for s in data:
        if s["rollno"] == rollno:
            data.remove(s)
            save_data(data)
            return {"message" : "student is deleted from database"}
    raise HTTPException(status_code=404, detail="Student not found")
        