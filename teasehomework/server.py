from flask import flask
app = Flask (__name__)

@app.route(hello'/hello/<name>')
def hello_name(name):
    return {"hello": name}

@app.route
def hello_world():
    return 'Hello, World!'