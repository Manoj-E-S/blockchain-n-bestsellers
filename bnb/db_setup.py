from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

_db = SQLAlchemy()
_migrate = Migrate()

def get_db():
    return _db

def get_migrate():
    return _migrate