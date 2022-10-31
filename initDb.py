from dbConnection import engine

from models import models


# create models

models.Base.metadata.create_all(bind=engine)