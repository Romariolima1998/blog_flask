from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config


db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(Config)

    db.init_app(app)

    from app.posts import post
    app.register_blueprint(post)

    return app


