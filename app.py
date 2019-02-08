#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['TESTING'] = True
app.config['ENV'] = 'development'
app.config.from_pyfile("flask.cfg")
print(f"{app.config}")


# # Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def hello_world():
    return render_template('index.html')
