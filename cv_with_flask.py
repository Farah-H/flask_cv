
from flask import Flask, jsonify, redirect, url_for, render_template
import base.html
import index.html
# create an instance of our app
app = Flask(__name__)

@app.route("/")  # localhost:5000 is default port for Flask
def home():
    # Homepage 
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1> "


@app.route("/login/") #localhost:5000/welcome/
def greet_user():
    return redirect(for_url('greet_user'))


@app.route("/linkedin/")
def linkedin():
    return render_template(linkedin.html)

@app.route
def 