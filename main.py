from fastapi import FastAPI



# init app

app = FastAPI()

# ##############

@app.get('/')

def home():
    return {
        "message" : "Hello world"
    }