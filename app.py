import os
import json
import pandas as pd
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, RedirectResponse, Response
from pydantic import BaseModel
import uvicorn
from joblib import load


class Student(BaseModel):
    BYSEX: int
    BYRACE: int
    BYSTLANG: int
    BYPARED: int
    BYINCOME: int
    BYURBAN: int
    BYREGION: int
    BYRISKFC: int
    BYS34A: int
    BYS34B: int
    BYWRKHRS: int
    BYS42: int
    BYS43: int
    BYTVVIGM: int
    BYS46B: int
    BYS44C: int
    BYS20E: int
    BYS87C: int
    BYS20D: int
    BYS23C: int
    BYS37: int
    BYS27I: int
    BYS90D: int
    BYS38A: int
    BYS20J: int
    BYS24C: int
    BYS24D: int
    BYS54I: int
    BYS84D: int
    BYS84I: int
    BYS85A: int


rus_clf = load("rus_clf.joblib")

app = FastAPI()

origins = [
    "http://127.0.0.1:63800",
    "https://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")


@app.route("/")
async def home():
    '''
    displays the home page
    '''
    return FileResponse("index.html")


@app.route("/student_success")
async def student_success():
    '''
    creates a student and stores it to the database
    '''
    return {
        "code": "success",
        "message": "student created"
    }


@app.route("/plotly")
async def plotly():
    '''
    diplay visualizations
    '''
    return {
        "code": "success",
        "message": "student created"
    }


@app.post("/predict")
async def predict(student: Student):

    student_list = []
    for i in student:
        student_list.append(i[1])

    X = [student_list]

    gpa_grade_bin = rus_clf.predict(X)[0]

    gpa_grade_dict = {
        0: "D or F",
        1: "C",
        2: "B",
        3: "A"
    }
    grade = gpa_grade_dict[gpa_grade_bin]
    
    proability_of_gpa_bin = rus_clf.predict_proba(X)[0][gpa_grade_bin]

    grade_proba = json.dumps({
        "grade": grade,
        "proability_of_gpa_bin": proability_of_gpa_bin
    })

    return Response(content=grade_proba, media_type="application/json")


@app.get("/get_student_data")
async def get_student_data():
    '''
    data route access
    '''

    file_path = os.path.join("clean_student_data.csv")

    df = pd.read_csv(file_path, index_col="STU_ID")
    json_compatible_df_data = jsonable_encoder(df.to_json())

    return Response(content=json_compatible_df_data, media_type="application/json")


if __name__=='__main__':
    uvicorn.run("app:app", reload=True)