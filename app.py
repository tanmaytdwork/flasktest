from flask import Flask

app = Flask(__name__)




@app.get("/data")
def get_data():
    return{"data":"this is all the data"}

@app.get("/")
def get_homepage():
    return{"data":"this is home page"}