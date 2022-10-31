from fastapi import Depends, FastAPI

from schemas import schemas
from dbConnection import SessionLocal

from sqlalchemy.orm import Session

import crud

app = FastAPI()


def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


#* create user //: endpoint
@app.post('/user' , response_model=schemas.UserBase)
async def createUser(request : schemas.CreateUser , db : Session = Depends(db)):
    user = await crud.create_user(db=db , user = request)
    return user