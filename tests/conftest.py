"""Pytest fixtures for Flask application testing."""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from pytest import fixture

from app import app as flask_app


@fixture
def app():
    """Provide Flask app instance for testing."""
    yield flask_app

@fixture
def client(app):
    """Provide Flask test client."""
    return app.test_client()