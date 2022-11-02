from sqlalchemy import Column, Integer , String
from database import Base


# * User Model

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer , unique=True , index=True , primary_key=True)
    username = Column(String)
    password = Column(String)