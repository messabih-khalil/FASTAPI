from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Candy(BaseModel):
    name : str
    recipe: str
    piece : Optional[bool] = False

# init app

app = FastAPI()


# start api #

@app.post('/candy')

def candy(request : Candy):
    return {
        'name' : request.name,
        'recipe' : request.recipe,
        'is_piece' : request.piece
    }