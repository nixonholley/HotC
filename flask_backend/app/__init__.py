import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.health import health_bp

# Config classes
from config import DevelopmentConfig, ProductionConfig

from dotenv import load_dotenv

# Load environment from .env file
load_dotenv()

# # better to init oustide of function to avoid cyclic imports
# db = SQLAlchemy()

def __init_app__(db):
    # init app
    app = Flask(__name__)

    # configure app based on environment
    env = os.getenv('ENV', 'development') # default to development
    if env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # db config
    db.init_app(app)

    # register blueprints
    app.register_blueprint(health_bp)

    return app