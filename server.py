from flask import Flask, redirect, render_template, url_for, session
from flask_oauth import OAuth
import os


# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = os.environ["CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = "a_seeeecrit"
oauth = OAuth()

@app.route("/")
def index():

    return render_template("index.html")

def main():
    app.run()


if __name__ == '__main__':
    main()