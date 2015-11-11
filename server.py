from flask import Flask, redirect, render_template, url_for, session, request
# from flask_oauth import OAuth
from oauth2client import client, crypt
import os
import requests


# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = os.environ["CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = "a_seeeecrit"
# oauth = OAuth()

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/tokencheck", methods=['POST'])
def tokencheck():
#     user_confirmation_data = self.request.get('data')
    user_confirm = request.form
    print user_confirm['aud']
    print type(GOOGLE_CLIENT_ID)
    if user_confirm["aud"] == GOOGLE_CLIENT_ID:
        print "success"
        return "success"
    else:
        return "fail"
    # r = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=')

    # try:
    #     idinfo = client.verify_id_token(token, CLIENT_ID)
    #     # If multiple clients access the backend server:
    #     if idinfo['aud'] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
    #         raise crypt.AppIdentityError("Unrecognized client.")
    #     if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
    #         raise crypt.AppIdentityError("Wrong issuer.")
    #     if idinfo['hd'] != APPS_DOMAIN_NAME:
    #         raise crypt.AppIdentityError("Wrong hosted domain.")
    # except crypt.AppIdentityError:
    #     # Invalid token
    #     userid = idinfo['sub']


def main():
    app.run()


if __name__ == '__main__':
    main()
