from flask import Flask, request
from time import sleep

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sleep3():
    sleep(0.5)
    return "Status: Success"

app.run()