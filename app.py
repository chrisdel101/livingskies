#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from flask import g
from flask_mail import Mail
from flask_mail import Message

import os

app = Flask(__name__)
# app.config.from_pyfile("settings.py")
app.config.from_pyfile("flask.cfg")
app.config.update(
    MAIL_SERVER=app.config['MAIL_SERVER'],
    MAIL_PORT=app.config['MAIL_PORT'],
    MAIL_USE_SSL=app.config['MAIL_USE_SSL'],
    MAIL_USERNAME=app.config['MAIL_USERNAME'],
    MAIL_PASSWORD = app.config['MAIL_PASSWORD']
)

mail = Mail(app)

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
        print(app.config['MAIL_PASSWORD'])
        print(app.config['MAIL_SERVER'])
        print(app.config['MAIL_USERNAME'])
        print(app.config['MAIL_PORT'])
        return render_template('contact.html')
    elif(request.method == 'POST'):
        if(not request.form.get('name') or not request.form.get('email') or not request.form.get('message')):
        # TODO
            print(request.form)
            return
        else:
            print(app.config['MAIL_PASSWORD'])
            print(app.config['MAIL_SERVER'])
            print(app.config['MAIL_USERNAME'])
            print(app.config['MAIL_PORT'])
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            msg = Message("Hello",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=["arssonist@yahoo.com"])
            mail.send(msg)
            return render_template('contact.html')
