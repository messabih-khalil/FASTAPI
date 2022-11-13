from typing import List
from fastapi import FastAPI , Query , Path
from pydantic import BaseModel , Field


app =FastAPI()

class BaseUser(BaseModel):
    username : str
    email : str

class UserResponse(BaseUser):
    id : int

class UserRequest(BaseUser):
    id : int
    password : str

class UserInDB(BaseUser):
    id : int
    hashed_password : str 


fake_user = []

# hash password
def hashPassword(password : str):
    return f"hashed:##@${password}"


# save to db
def saveToDb(user : UserRequest):
    hashed_password = hashPassword(user.password)
    fake_new_user = UserInDB(**user.dict() , hashed_password = hashed_password)
  
    return fake_new_user

# add new user 

@app.post('/user' , response_model=UserInDB)
def createUser(request : UserRequest):
    fake_user = saveToDb(request)

    return fake_user