from datetime import datetime
from fastapi import FastAPI , HTTPException, Request , status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

# custom exception 
class NotExistException(Exception):
    def __init__(self , name : str):
        self.name = name


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

    
app = FastAPI()


@app.exception_handler(NotExistException)
def not_exist(request : Request , exc : NotExistException):
    return JSONResponse(
            content=f"{exc.name} is not exist",
            status_code=status.HTTP_404_NOT_FOUND
    )

# names 

names = ['tars' , 'aldn' , 'fryl']

# get name
@app.get('/name')
def getName(name : str | None):
    if name not in names:
        raise NotExistException(name)
    
    return {
        "name" : name
    }


# jsonable item