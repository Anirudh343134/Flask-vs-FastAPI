from fastapi import FastAPI
from time import sleep
import uvicorn

app = FastAPI()

@app.get('/')
def sleep3():
    sleep(0.5)
    return {"Status": "Success"}


@app.post('/')
def sleep3():
    sleep(0.5)
    return {"Status": "Success"}

uvicorn.run(app)