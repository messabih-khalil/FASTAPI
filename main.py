from fastapi import FastAPI



# init app

app = FastAPI()

# ##############

@app.get('/')

def home():
    return {
        "message" : "Hello world"
    }


# about api

@app.get('/about')

def about():
    return {
        'data' : "about"
    }