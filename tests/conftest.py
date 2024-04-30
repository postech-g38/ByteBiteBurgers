from typing import Any, Generator
import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete

from src.app import app
from src.adapters.database.settings import sync_engine, get_session
from src.adapters.database.models.base_model import BaseModel

from tests.manage_database import load_database_mock


@pytest.fixture(scope='session')
def sync_client() -> Generator[TestClient, None, None]:
    sync_test_client = TestClient(
        app=app,
        base_url=f"http://localhost:{os.getenv('APPLICATION_PORT')}",
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    )
    with sync_test_client as _client:
        yield _client    


@pytest.fixture(scope='session')
def create_database_tables():
    BaseModel.metadata.create_all(sync_engine)
    yield
    BaseModel.metadata.drop_all(sync_engine)


@pytest.fixture(scope='function')
def database(create_database_tables) -> Generator[Session, None, None]:
    with get_session() as database_session:
        yield database_session
        for table in BaseModel.metadata.sorted_tables:
            database_session.execute(delete(table))
