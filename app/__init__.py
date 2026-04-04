import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()


def create_app() -> Flask:
    """
    Application factory that configures Flask for different environments
    (development vs production) based on environment variables.
    """
    
    # Load environment variables from .env (for local/dev)
    load_dotenv()

    from .config import DevelopmentConfig, ProductionConfig

    app = Flask(__name__)

    flask_env = os.environ.get("FLASK_ENV", "development").lower()
    if flask_env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    
    with app.app_context():
        from . import models  
        from .routes import register_blueprints

        register_blueprints(app)
        db.create_all()

    return app

