from typing import List
from fastapi import Depends, FastAPI, HTTPException , status

from sqlalchemy.orm import Session

from models import models
from schemas import schemas

from database import SessionLocal, engine

app = FastAPI()


models.Base.metadata.create_all(bind = engine)

def db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()


@app.get('/')
def home():
    return {
        "message" : "hello world"
    }

# * Create user 
@app.post('/user')
def createUser(request : schemas.CreateUserSchema , db : Session = Depends(db) , status_code=status.HTTP_201_CREATED):
    user = models.User(id = request.id , username = request.username , password = request.password)
    
    # insert new user to db

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# * get new user

@app.get('/user' , response_model=List[schemas.UserResponse])
def getUser(db : Session = Depends(db)):
    user = db.query(models.User).all()
    
    return user

# * get user by id

@app.get('/user/{id}' , status_code=status.HTTP_200_OK)
def getMyUser(id : int , db : Session = Depends(db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user

    raise HTTPException(detail='user not exist' , status_code=status.HTTP_404_NOT_FOUND)


# * delete user 

@app.delete('/user/{id}')
def deleteUser(id : int ,db : Session = Depends(db)):
    user = db.query(models.User).filter(models.User.id == id)

    if user :
        user.delete(synchronize_session=False)
        db.commit()
        return {
            "message" : "deleted"
        }

    raise HTTPException(detail='user not exist' , status_code=status.HTTP_404_NOT_FOUND)