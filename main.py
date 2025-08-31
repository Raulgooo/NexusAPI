from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class User(BaseModel):  #User class
    user: str
    password: str

app = FastAPI(title="NexusAPI", version="1.0.0")

@app.post("/login") #Endpoint to login
async def login(user: User):
    driver = webdriver.Chrome()
    ##if user.user == "admin" and user.password == "admin":
        #eturn {"message": "Login successful"}
        ##selenium