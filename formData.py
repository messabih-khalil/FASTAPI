from fastapi import FastAPI , Form
from pydantic import BaseModel

# app

# 
class Car(BaseModel):
    name : str = Form()
    owner : str = Form()

app = FastAPI()

# post car

@app.post('/car' , response_model=Car)
def car(request : Car):
    new_car = Car(**request.dict())
    return new_car
