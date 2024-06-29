from .app_setup import get_app
from .db_setup import (
    get_db, get_migrate
)
from .schema import (
    User, Book, Rating, Exchange, TrainableBook, Message, ServerStats
)
from flask_cors import CORS


def create_app():
    
    app = get_app()
    CORS(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173/"}})

    db = get_db()
    db.init_app(app)

    migrate = get_migrate()
    migrate.init_app(app, db)

    
    # Register blueprints
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    
    from .books.routes import book_bp
    app.register_blueprint(book_bp)
    
    return app
