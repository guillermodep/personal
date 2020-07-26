from flask import render_template
from flask import Flask, render_template
from app import app
from app.forms import LoginForm

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")


"""
@app.route('/index')
def index():
    return "<h2><center>Openshift - K8s Multi Cloud Management</center></h2>"
"""