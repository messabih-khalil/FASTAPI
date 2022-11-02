from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# * Database url
DATABASE_URL = 'sqlite:///./data.db'

# * Create database engine
engine = create_engine(DATABASE_URL , connect_args={"check_same_thread" : False})

# * base orm
Base = declarative_base()

# * Create Session maker
SessionLocal = sessionmaker(bind = engine , autocommit=False , autoflush=False)