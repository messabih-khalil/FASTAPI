from pydantic import BaseModel

# * User create schema
class CreateUserSchema(BaseModel):
    id : int
    username : str
    password : str

    class Config:
        orm_mode = True

# * User Schema
class UserSchema(BaseModel):
    id : int
    username : str

    class Config:
        orm_mode = True

# * Response model :=> user
class UserResponse(BaseModel):
    username : str

    class Config:
        orm_mode = True