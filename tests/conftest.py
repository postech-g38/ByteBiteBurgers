from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient

from src.app import app
from pymongo import MongoClient
from src.settings import get_settings
from src.adapters.database.settings import get_session

import socket



@pytest.fixture(scope='session')
def client() -> Generator[TestClient, None, None]:
    sync_test_client = TestClient(
        app=app,
        base_url=f"http://{socket.gethostbyname(socket.gethostname())}:8000",
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    )
    with sync_test_client as _client:
        yield _client    


@pytest.fixture
def database():
    client = MongoClient(
        host=get_settings().database_settings.sync_uri, 
        port=get_settings().database_settings.database_port,
        maxPoolSize=50,
        minPoolSize=10,
        maxIdleTimeMS=3,
        waitQueueTimeoutMS=10
    )
    db = client['mongo']
    yield db
    client.drop_database('mongo')

@pytest.fixture
def database_session():
    with get_session() as sess:
        yield sess
