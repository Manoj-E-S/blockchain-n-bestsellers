from flask import Blueprint, redirect, session
import os

from .google_oauth_setup import get_auth_url, get_credentials

PATH_TO_CLIENT_SECRET = os.path.join(os.path.dirname(__file__), "../.secrets/client_secret.json")
SCOPES = ['https://www.googleapis.com/auth/books']

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/")
def auth():
    return "hello from auth"

@auth_bp.route("/login")
def login():
    authorization_url, state = get_auth_url(
            path_to_client_secret=PATH_TO_CLIENT_SECRET, 
            redirect_uri="http://localhost:3000/auth/dashboard", 
            scopes=SCOPES
        )
    session['state'] = state
    print(1)
    print(authorization_url)
    return redirect(authorization_url)

@auth_bp.route("/logout")  
def logout():
    return "logout"

@auth_bp.route("/loggedin")
def loggedin():
    return "loggedin"

@auth_bp.route('/dashboard')
def dashboard():
    print(2)
    credentials = get_credentials(
            path_to_client_secret=PATH_TO_CLIENT_SECRET,
            scopes=SCOPES
        )
    print(3)
    session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
    return "callbackoauth"