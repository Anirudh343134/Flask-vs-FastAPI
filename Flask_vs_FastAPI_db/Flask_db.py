from flask import Flask
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def home():
    return "<center><h1>HOME</h1</center>"


@app.route('/<id>')
def query(id):
    db_path = os.path.join(currentdirectory, "IIT_admissions.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    query1 = "SELECT * FROM student_data where id = " + str(id)
    result = cursor.execute(query1)
    return str(result.fetchall())

app.run(debug=True)
