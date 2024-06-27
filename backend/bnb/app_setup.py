import os
from urllib.parse import quote

from flask import Flask

from dotenv import load_dotenv
load_dotenv("../.env")

def get_jwt_secret():
    return os.getenv("JWT_SECRET", "")

def get_host():
    HOST = os.getenv("DEV_HOST", "")
    return HOST

def get_port():
    PORT = os.getenv("DEV_PORT", "")
    return PORT

def get_db_uri_cloud():
    DB_URI = os.getenv("CLOUD_DB_URI", "")
    return DB_URI

def get_db_uri_local():
    db_user = os.getenv("DB_USER", "")
    db_pswd = quote(os.getenv("DB_PASSWORD", ""))
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "")
    local_db = os.getenv("LOCAL_DB", "")
    db_connector = os.getenv("DB_CONNECTOR", "")
    print(f"db: {local_db}({db_name})@{db_host}:{db_port}")
    DB_URI = f'{local_db}+{db_connector}://{db_user}:{db_pswd}@{db_host}:{db_port}/{db_name}'
    print(f"DB_URI: {DB_URI}")
    return DB_URI

def get_db_uri():
    env = os.getenv("FLASK_ENV", "dev")
    if env == "prod":
        return get_db_uri_cloud()
    return get_db_uri_local()

def get_app():
    app = Flask("bnb")
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print(os.getenv("FLASK_APP_SECRET_KEY"))
    app.config['SECRET_KEY'] = os.getenv("FLASK_APP_SECRET_KEY")
    app.secret_key = os.getenv("FLASK_APP_SECRET_KEY")
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    return app

