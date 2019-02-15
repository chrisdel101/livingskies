#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from flask import g
from flask_mail import Mail

import os

app = Flask(__name__)
mail = Mail(app)


app.config.from_pyfile("settings.py")

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

@app.route('/contact', methods=['GET','POST' ])
def render_contact():
    if(request.method == 'GET'):
        print('Hello')
        return render_template('contact.html')
    elif(request.method == 'POST'):
        # if(not request.form.name or not request.form.email or not request.form.message):
        #     # TODO
        #     print('missing info')

        # if:
        name = request.form[0][0]
        email = request.form[1[0]]
        message = request.form[2][0]
        print(f"{name, email,message}")
        # print(request.form[])
        return render_template('contact.html')
