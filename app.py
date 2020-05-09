# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
from typing import List
from fastapi import FastAPI, Request, Depends, BackgroundTasks, Form, Header, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
# from database import SessionLocal, engine
from pydantic import BaseModel
# from sqlalchemy.orm import Session
# import models
import uvicorn
from joblib import load


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
    expose_headers=["*"]
)

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


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    '''
    displays the home page
    '''
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/student_success")
async def student_success(request: Request):

    return templates.TemplateResponse("form.html", {"request": request})


@app.get("/prediction")
async def prediction(request: Request, BYSEX: int = Form(default=0),
    BYRACE: int = Form(default=0), BYSTLANG: int = Form(default=0), BYPARED: int = Form(default=0),
    BYINCOME: int = Form(default=0), BYURBAN: int = Form(default=0), BYREGION: int = Form(default=0),
    BYRISKFC: int = Form(default=0), BYS34A: int = Form(default=0), BYS34B: int = Form(default=0),
    BYWRKHRS: int = Form(default=0), BYS42: int = Form(default=0), BYS43: int = Form(default=0),
    BYTVVIGM: int = Form(default=0), BYS46B: int = Form(default=0), BYS44C: int = Form(default=0),
    BYS20E: int = Form(default=0), BYS87C: int = Form(default=0), BYS20D: int = Form(default=0),
    BYS23C: int = Form(default=0), BYS37: int = Form(default=0), BYS27I: int = Form(default=0),
    BYS90D: int = Form(default=0), BYS38A: int = Form(default=0), BYS20J: int = Form(default=0),
    BYS24C: int = Form(default=0), BYS24D: int = Form(default=0), BYS54I: int = Form(default=0),
    BYS84D: int = Form(default=0), BYS84I: int = Form(default=0), BYS85A: int = Form(default=0)):
    
    student_list = [BYSEX, BYRACE, BYSTLANG, BYPARED, BYINCOME, BYURBAN, BYREGION, BYRISKFC, BYS34A,
    BYS34B, BYWRKHRS, BYS42, BYS43, BYTVVIGM, BYS46B, BYS44C, BYS20E, BYS87C, BYS20D, BYS23C, BYS37,
    BYS27I, BYS90D, BYS38A, BYS20J, BYS24C, BYS24D, BYS54I, BYS84D, BYS84I, BYS85A]
    
    X = [student_list]
    
    gpa_range_bin = rus_clf.predict(X)[0]
    
    gpa_range_dict = {
        0: ["0.00 - 1.50", "D or F"],
        1: ["1.51 - 2.00", "C"],
        2: ["2.01 - 3.50", "B"],
        3: ["3.51 - 4.00", "A"]
    }
    
    gpa_range = gpa_range_dict[gpa_range_bin][0]
    equivalent_letter_grade = gpa_range_dict[gpa_range_bin][1]
    probability_of_gpa_range = str(rus_clf.predict_proba(X)[0][gpa_range_bin] * 100) + "%"
    
    return templates.TemplateResponse("prediction.html", {"request": request, "gpa_range": gpa_range, "equivalent_letter_grade": equivalent_letter_grade, "probability_of_gpa_range" : probability_of_gpa_range})


@app.post("/predict")
async def predict(student: Student):
    student_list = []
    for i in student:
        student_list.append(i[1])
    X = [student_list]
    gpa_range_bin = rus_clf.predict(X)[0]
    gpa_range_dict = {
        0: ["0.00 - 1.50", "D or F"],
        1: ["1.51 - 2.00", "C"],
        2: ["2.01 - 3.50", "B"],
        3: ["3.51 - 4.00", "A"]
    }
    gpa_range = gpa_range_dict[gpa_range_bin][0]
    equivalent_letter_grade = gpa_range_dict[gpa_range_bin][1]
    probability_of_gpa_range = rus_clf.predict_proba(X)[0][gpa_range_bin]
    grade_range_proba = json.dumps({
        "gpa_range": gpa_range,
        "equivalent_letter_grade": equivalent_letter_grade,
        "probability_of_gpa_range": probability_of_gpa_range
    })
    return Response(content=grade_range_proba, media_type="application/json")


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