# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
from fastapi import FastAPI, Request, Depends, BackgroundTasks, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
# from database import SessionLocal, engine
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# import models
import uvicorn
from joblib import load

file_path = "index.html"

rus_clf = load("rus_clf.joblib")

app = FastAPI(debug=True)

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

# models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(item_id="templates/index.html"):
    '''
    displays the home page
    '''
    return FileResponse(item_id)


@app.api_route("/student_success", methods=["GET", "POST"])
async def student_success(request: Request, BYSEX: int = Form(default=''),
    BYRACE: int = Form(default=''),BYSTLANG: int = Form(default=''),BYPARED: int = Form(default=''),
    BYINCOME: int = Form(default=''),BYURBAN: int = Form(default=''),BYREGION: int = Form(default=''),
    BYRISKFC: int = Form(default=''),BYS34A: int = Form(default=''),BYS34B: int = Form(default=''),
    BYWRKHRS: int = Form(default=''),BYS42: int = Form(default=''),BYS43: int = Form(default=''),
    BYTVVIGM: int = Form(default=''),BYS46B: int = Form(default=''),BYS44C: int = Form(default=''),
    BYS20E: int = Form(default=''),BYS87C: int = Form(default=''),BYS20D: int = Form(default=''),
    BYS23C: int = Form(default=''),BYS37: int = Form(default=''),BYS27I: int = Form(default=''),
    BYS90D: int = Form(default=''),BYS38A: int = Form(default=''),BYS20J: int = Form(default=''),
    BYS24C: int = Form(default=''),BYS24D: int = Form(default=''),BYS54I: int = Form(default=''),
    BYS84D: int = Form(default=''),BYS84I: int = Form(default=''),BYS85A: int = Form(default='')
):
    if request.method == "GET":
        return FileResponse("templates/form.html")
    if request.method == "POST":

        
        student_list = [BYSEX, BYRACE, BYSTLANG, BYPARED, BYINCOME, BYURBAN, BYREGION, BYRISKFC, BYS34A,
        BYS34B, BYWRKHRS, BYS42, BYS43, BYTVVIGM, BYS46B, BYS44C, BYS20E, BYS87C, BYS20D, BYS23C, BYS37,
        BYS27I, BYS90D, BYS38A, BYS20J, BYS24C, BYS24D, BYS54I, BYS84D, BYS84I, BYS85A]

        X = [student_list]

        gpa_range_bin = rus_clf.predict(X)[0]

        gpa_range_dict = {
            0: "0.00 - 1.50 (Equivalent to D or F average)",
            1: "1.51 - 2.00 (Equivalent to C average)",
            2: "2.01 - 3.50 (Equivalent to B average)",
            3: "3.51 - 4.00 (Equivalent to A average)"
        }

        gpa_range = gpa_range_dict[gpa_range_bin]
        
        probability_of_gpa_range = rus_clf.predict_proba(X)[0][gpa_range_bin]

        grade_range_proba = json.dumps({
            "gpa_range": gpa_range,
            "probability_of_gpa_range": probability_of_gpa_range
        })
        print(grade_range_proba)

        return templates.TemplateResponse("form.html", {"request": Request, "gpa" : gpa_range, "probability" : probability_of_gpa_range})




# @app.get("/student_success/")
# async def render_form():
#     return FileResponse("templates/form.html")

# @app.post("/student_success/")
# async def submit_form(BYSEX: str = Form(default=''),
#     BYRACE: str = Form(default='')):
#     return FileResponse("templates/form.html")

@app.route("/plotly")
async def plotly():
    '''
    diplay visualizations
    '''
    return {
        "code": "success",
        "message": "student created"
    }


<<<<<<< HEAD
=======
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


>>>>>>> master
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