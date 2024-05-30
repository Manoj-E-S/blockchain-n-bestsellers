from flask import Blueprint, redirect, session, request
import os

from .google_oauth_setup import get_auth_url, get_credentials
from ..db_setup import get_db
from ..schema import User 
from ..Utils.hash import hash_password


_db = get_db()
PATH_TO_CLIENT_SECRET = os.path.join(os.path.dirname(__file__), "../.secrets/client_secret.json")
SCOPES = ['https://www.googleapis.com/auth/books', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/")
def auth():
    return "hello from auth"

# @auth_bp.route('/signup', methods=['POST'])
# def signup():
#     if request.is_json:
#         try:
#             data = request.get_json()
#             new_user = User(name=data['name'], email=data['email'], password=hash_password(data['password']), location=data['location'], contact_no=data['contact_no'], bio=data['bio'])
#             _db.session.add(new_user)
#             _db.session.commit()
#             return {"message": f"User {new_user.username} has been created successfully.", "user_id": new_user.id}, 201
#         except Exception as e:
#             return {"error": str(e)}, 500
#     else:
#         return {"error": "The request payload is not in JSON format"}, 400


@auth_bp.route("/login", methods=["POST"])
def login():
    
    return "login"

@auth_bp.route("/googlelogin")
def google_login():
    authorization_url, state = get_auth_url(
            path_to_client_secret=PATH_TO_CLIENT_SECRET, 
            redirect_uri="http://localhost:3000/auth/dashboard", 
            scopes=SCOPES
        )
    session['state'] = state
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
    credentials = get_credentials(
            path_to_client_secret=PATH_TO_CLIENT_SECRET,
            scopes=SCOPES
        )
    # print all the credentials convert to dict TODO: remove this when deployed
    print(credentials.__dict__)
    session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
    return "callbackoauth"