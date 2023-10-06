import pytest
from fastapi.testclient import TestClient

from src.app import run_app


@pytest.fixture(scope='session')
def sync_client():
    return TestClient(
        app=run_app(),
        base_url='localhost:8000'
        )
