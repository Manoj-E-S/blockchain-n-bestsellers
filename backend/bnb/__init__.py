from .app_setup import get_app
from .db_setup import (
    get_db, get_migrate
)
from .schema import (
    User, Book, Rating, Exchange, TrainableBook, Message, ServerStats
)

def create_app():
    
    app = get_app()

    db = get_db()
    db.init_app(app)

    migrate = get_migrate()
    migrate.init_app(app, db)

    
    # Register blueprints
    # from .auth.routes import auth_bp
    # from .recommend.routes import recommend_bp
    
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(recommend_bp)
    
    return app
