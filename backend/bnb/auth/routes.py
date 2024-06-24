from flask import Blueprint, redirect, session, request
import os

from .google_oauth_setup import get_auth_url, get_credentials
from ..db_setup import get_db
from ..schema import User 
from ..Utils.hash import hash_password, verify_password
from ..Utils.jwt import encode, decode
from ..Utils.oauth import get_name_and_email


_db = get_db()
PATH_TO_CLIENT_SECRET = os.path.join(os.path.dirname(__file__), "../.secrets/client_secret.json")
SCOPES = ['https://www.googleapis.com/auth/books', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/")
def auth():
    return "hello from auth"

@auth_bp.route('/signup', methods=['POST'])
def signup():
    if request.is_json:
        try:
            data = request.get_json()
            new_user = User(name=data['name'], email=data['email'], password=hash_password(data['password']), location=data['location'], contact_no=data['contact_no'], bio=data['bio'])
            token = encode({"user_id": new_user.uId})
            _db.session.add(new_user)
            _db.session.commit()
            return {"message": f"User {new_user.name} has been created successfully.", "token": token}, 201
        except Exception as e:
            print(e)
            return {"error": str(e)}, 500
    else:
        return {"error": "The request payload is not in JSON format"}, 400


@auth_bp.route("/login", methods=["POST"])
def login():
    if request.is_json:
        try:
            data = request.get_json()
            user = User.query.filter_by(email=data['email']).first()
            if user and verify_password(data['password'], user.password):
                token = encode({"user_id": user.uId})
                return {"message": f"Welcome back {user.name}", "token": token}, 200
            else:
                return {"error": "Invalid email or password"}, 401
        except Exception as e:
            print(e)
            return {"error": str(e)}, 500
    else:
        return {"error": "The request payload is not in JSON format"}, 400


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
    name, email = get_name_and_email(credentials)    
    print(name, email)
    return "callbackoauth"