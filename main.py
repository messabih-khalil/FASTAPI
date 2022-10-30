from typing import Optional
from fastapi import FastAPI



# init app

app = FastAPI()


# start api #

@app.get('/comments')

def comments(limit : int = 10 , date : str = '2022-12-12' , order : Optional[str] = None):
    
    return{
        "comments" : [
            {
                '1' : 'h',
                '2' : 'e',
                '3' : 'l',
                '4' : 'l',
                '5' : 'o',
            },
        ],

        'limit' : limit,
        'date' : date
    }