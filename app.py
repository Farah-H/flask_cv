
from flask import Flask, redirect, url_for, render_template
# create an instance of our app

app = Flask(__name__)

@app.route("/") 
def home():
    # Homepage 
    return render_template('homepage.html')


# this doesn't work, need to fix
@app.route("/login/")
def greet_user():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)