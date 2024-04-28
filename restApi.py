from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("Welcome to Flask Application")

