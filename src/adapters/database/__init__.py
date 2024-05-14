from typing import AsyncGenerator

from sqlalchemy.orm.session import Session

from src.adapters.database.settings import get_session


async def get_database_session() -> AsyncGenerator[Session, None]:
    with get_session() as sess:
        yield sess
