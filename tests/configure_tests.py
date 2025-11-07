from pytest import fixture
from app import app as flask_app

@fixture
def app():
    yield flask_app

@fixture
def client(app):
    return app.test_client()