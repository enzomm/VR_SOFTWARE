from importlib import import_module
from flask import Flask
from app.ext import config
from app.ext.database import configure_database
from flask_cors import CORS


def register_blueprints(app):
    """Register all blueprints dynamically"""
    for module_name in (        
        "home",
    ):
        module = import_module("app.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)


def minimal_app():
    """Factory to create a minimal Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    return app


def create_app():
    """Factory to create a Flask app"""
    app = minimal_app()    
    CORS(app, origins="*") # Allow any domain

    # Load extensions
    config.load_extensions(app)

    # Configure database
    configure_database(app)

    # Register Blueprints
    register_blueprints(app)

    return app
