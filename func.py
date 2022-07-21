#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""
# USING FUNCTION INSIDE THE MODEL
from fastapi import FastAPI

from pydantic import BaseModel

class Profile(BaseModel):
    name:str 
    email:str 
    age:int
    
class Product(BaseModel):
    name:str 
    price:int 
    discount:int 
    discounted_price:float 
    
app=FastAPI()

@app.post('/addproduct')
def addproduct(product:Product):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return product 

@app.get('/user/admin')
def admin():
    return {"This is admin page"}

@app.post("/adduser")
def adduser(profile:Profile):
    return profile 

