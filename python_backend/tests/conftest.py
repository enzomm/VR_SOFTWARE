from app import create_app, minimal_app, register_blueprints
from app.ext.database import db
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
        
        
@pytest.fixture(scope="module")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="module")
def mini_app():
    app = minimal_app()
    register_blueprints(app)    
    return app


@pytest.fixture
def database(mini_app):
    mini_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///development.db"
    db.init_app(mini_app)
    with mini_app.app_context():
        db.create_all()
        db.session.commit()
        yield db
        db.drop_all()


@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
