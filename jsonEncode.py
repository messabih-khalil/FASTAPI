from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    username : str
    dateOfBirth : date


# app

app = FastAPI()

@app.post('/add-user/')
def createUser(request : User):
    josnable_data = jsonable_encoder(request)
    print(josnable_data)