from typing import Generator

from src.adapters.database.settings import get_session


def get_database_session() -> Generator:
    with get_session() as sess:
        yield sess
