#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""

from fastapi import FastAPI, Path

app=FastAPI()

students ={
    1:{
       "name":"sathwik",
       "age":"24",
       "company":"vsoft"
       }
}

@app.get("/")
def index():
    return{"name":"details"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id] 



@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None, description="The ID of the student you want to view",gt=0)):
    return students[student_id]







