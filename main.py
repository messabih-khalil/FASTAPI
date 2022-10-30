from fastapi import FastAPI



# init app

app = FastAPI()


# start api #

@app.get('/age/{age}')
def ageInDays(age : int):
    
    age_in_days = age * 365

    return {
        'age' : age,
        'ageInDays' : age_in_days
    }