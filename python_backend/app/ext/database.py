from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True, render_as_batch=True)    
    if app.config["ENV"] == "production" or app.config["ENV"] == "test":
        app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}@{app.config['DB_HOST']}:{app.config['DB_PORT']}/{app.config['DB_NAME']}"


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        with app.app_context():
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()
