from fastapi import FastAPI , Query , Path


# app

app = FastAPI()

# query params with validation

###
# str | none
# length with Query class
###
@app.get('/products/')
def products(name : str | None = Query(default=None, max_length=50)):
    
    return {
        'product_name' : name
    }


# path-params-numeric-validations

@app.get('/users/{id}')
def user(id : int = Path(tile="THe id of the user")):
    return {
        "user_id" : id
    }
