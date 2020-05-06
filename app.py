# -*- coding: utf-8 -*-
import os
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from database import SessionLocal, engine
# from pydantic import BaseModel 
from sqlalchemy.orm import Session
import models
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

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

#home screen
@app.route("/")
async def home():
    '''
    displays the home page
    '''
    return FileResponse(file_path)

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

@app.route("/data")
async def create_student():
    '''
    data route access
    '''
    return {
        "code": "success",
        "message": "student created"
    }

if __name__=='__main__':
    uvicorn.run(app)