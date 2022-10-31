
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dbConnection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer , primary_key = True , index = True)
    username = Column(String)
    email = Column(String , index=True , unique=True)
    password = Column(String)
    is_superuser = Column(Boolean , default=False)
     
    posts = relationship('Post' , back_populates="user")

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer , primary_key = True , index = True)
    title = Column(String)
    description = Column(String)

    user = relationship('User' , back_populates="posts")