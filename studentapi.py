#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:09:06 2022

@author: sathwik
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/get_student/")
def get_student():
    return {"name": "sathwik"}
