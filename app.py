#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import g
import os

app = Flask(__name__)

app.config.from_pyfile("settings.py")

print(f"{app.config}")
# # Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/services')
def render_services():
    return render_template('services.html')

@app.route('/about')
def render_about():
    return render_template('about.html')

@app.route('/contact')
def render_contact():
    return render_template('contact.html')
