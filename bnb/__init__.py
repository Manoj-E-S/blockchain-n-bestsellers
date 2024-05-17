# https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/ [REFER HERE]

import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)\
    
    # Development-Instance-Config
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # Override with Production-Instance-Config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Override with Testing-Instance-Config
        app.config.from_mapping(test_config)

    # Create instance directory if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Routing
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import recommend
    app.register_blueprint(recommend.bp)
    app.add_url_rule('/recommend', endpoint='recommend_popular')

    return app