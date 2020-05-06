# -*- coding: utf-8 -*-
import os
import pandas as pd
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
# from database import SessionLocal, engine
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# import models
import uvicorn

file_path = "index.html"

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

# templates = Jinja2Templates(directory="templates")

#home screen
# @app.route("/")
# async def home():
#     '''
#     displays the home page
#     '''
#     return FileResponse(file_path)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


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


# @app.route("/get_student_data")
@app.get("/get_student_data")
async def get_student_data():
    '''
    data route access
    '''

    file_path = os.path.join("clean_student_data.csv")

    df = pd.read_csv(file_path, index_col="STU_ID")
    json_compatible_df_data = jsonable_encoder(df.to_json())

    return JSONResponse(content=json_compatible_df_data)


if __name__=='__main__':
    uvicorn.run(app)