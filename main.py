from typing import List
from fastapi import FastAPI , Query , Path
from pydantic import BaseModel , Field


app =FastAPI()

fake_users = [
    {
        "id" : 1,
        "username" : "tars",
        "email" : "tars@gmail.com",
        "password" : "123456789"
    },
    {
        "id" : 2,
        "username" : "aldin",
        "email" : "aldin@gmail.com",
        "password" : "123456789"
    }
]


class User(BaseModel):
    # id : int
    username : str
    email : str

class CreateUser(BaseModel):
    username : str
    email : str
    password : str

# add user
@app.post("/user" , response_model=User)
def addUser(request : CreateUser):
    
    new_user = {
        "id" : 3,
        "username" : request.username,
        "email" : request.email,
        "password" : request.password
    }
    fake_users.append(new_user)

    return new_user


# get users
@app.get("/user" , response_model=list[User])
def allUsers():
    return fake_users
# get user
@app.get('/user/{id}' , response_model=User)
def getUser(id : int | None):
    user = [a for a in fake_users if a["id"] in id]
    print(user)
    return user

# update User

# delete user

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]