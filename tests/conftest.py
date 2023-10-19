import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.adapters.database.settings import sync_engine
from src.adapters.database.models.base_model import BaseModel

from tests.manage_database import load_database_mock


@pytest.fixture(scope='session')
def sync_client():
    with TestClient(
        app=app,
        base_url='http://localhost:8000',
        headers={'Content-Type': 'application/json'}
    ) as _client:
        yield _client


@pytest.fixture(scope='function')
def create_database():
    """Clear data first, ensure tables are empty, create, and after store values on db to check"""
    BaseModel.metadata.drop_all(bind=sync_engine)
    BaseModel.metadata.create_all(bind=sync_engine)


@pytest.fixture(scope='function')
def load_database():
    load_database_mock()
