from pydantic import BaseModel

from models.models import Post


class UserBase(BaseModel):
    username : str
    email : str
    is_active : bool

    class Config:
        orm_mode = True



class CreateUser(UserBase):
    id : int
    password : str
    # items : list[Post] = []


class PostBase(BaseModel):
    id : int
    title : str
    description : str

    user : int

    class Config:
        orm_mode = True

class CreatePost(PostBase):
    pass

class GetPost(PostBase):
    pass
