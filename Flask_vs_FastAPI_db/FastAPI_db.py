from fastapi import FastAPI
import sqlite3
import os
import uvicorn

app = FastAPI()
currentdirectory = os.path.dirname(os.path.abspath(__file__))

@app.get('/')
def home():
    return {"Location": "Home"}

@app.get('/{id}')
async def query(id: int):
    db_path = os.path.join(currentdirectory, 'IIT_admissions.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    query1 = "SELECT * FROM student_data WHERE id = " + str(id)
    result = cursor.execute(query1)
    return str(result.fetchall())

uvicorn.run(app)