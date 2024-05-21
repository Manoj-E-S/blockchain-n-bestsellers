from flask import Flask
from .db_setup import *
from dotenv import load_dotenv
import os
from .schema import User, Book, Rating, Exchange, TrainableBook, Message, ServerStats, user_messages

load_dotenv()
db = get_db()
migrate = get_migrate()

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)

    
    # Register blueprints
    # from .auth.routes import auth_bp
    # from .recommend.routes import recommend_bp
    
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(recommend_bp)
    
    return app
