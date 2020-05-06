# -*- coding: utf-8 -*-
import os
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
# from fastapi.responses import FileResponse
from database import SessionLocal, engine
# from pydantic import BaseModel 
from sqlalchemy.orm import Session
import models
import uvicorn

# class ModelName(str, Enum):
#     alexnet = "alexnet"
file_path = "index.html"

app = FastAPI(debug=True)

origins = [
    "http://127.0.0.1:63800",
    "http://127.0.0.1:62862",
    "http://127.0.0.1:62933",
    "https://127.0.0.1:50541",
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
@app.get("/")
async def home():
    '''
    displays the home page
    '''
    return FileResponse(file_path)

@app.post("/student")
async def create_student():
    '''
    creates a student and stores it to the database
    '''
    return {
        "code": "success",
        "message": "student created"
    }

# #plotly route to display visualizations
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# data route which when requested, 
# will return specific requested data,
# that we used to build our project, in a JSON format
# async def data():
#     return {"user_id": "the current user"}

if __name__=='__main__':
    uvicorn.run(app)