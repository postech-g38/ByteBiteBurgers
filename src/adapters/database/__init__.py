from typing import Generator

from sqlalchemy.orm.session import Session

from src.adapters.database.settings import get_session


def get_database_session() -> Generator[Session, None, None]:
    with get_session() as sess:
        yield sess
