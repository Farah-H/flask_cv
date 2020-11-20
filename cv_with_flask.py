
from flask import Flask, redirect, url_for, render_template
import base.html
import index.html
# create an instance of our app
app = Flask(__name__)

@app.route("/") 
def home():
    # Homepage 
    return render_template(homepage.html)


# this doesn't work, need to fix
@app.route("/login/")
def greet_user():
    return render_template(login.html)


@app.route("/linkedin/")
def linkedin():
    return render_template(linkedin.html)

@app.route("/github/")
def github():
    return render_template(github.html)

