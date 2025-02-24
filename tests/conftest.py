import pytest
import sys
import os

# Ensure the root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from instance.config import TestConfig
from website import create_app, db

import pytest

@pytest.fixture(scope="session")
def app():
    """Creates and configures a new app instance for each test session."""
    app = create_app()
    app.config.from_object(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
