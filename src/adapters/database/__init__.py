from src.adapters.database.settings import get_session


def get_database_session():
    with get_session() as sess:
        yield sess
