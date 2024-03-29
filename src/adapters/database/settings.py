import logging

from contextlib import contextmanager


from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy import text

from src.settings import  get_settings
from src.adapters.database.models.base_model import BaseModel


_logger = logging.getLogger(__name__)


def _create_sync_engine():
    return create_engine(
        url=get_settings().database_settings.unittest_sync_uri,
        pool_size=10, #  get_settings().database.database_pool_size,
        max_overflow=20, #  get_settings().database.database_max_overflow,
        pool_pre_ping=True,
        pool_recycle=3600, #  get_settings().database.database_pool_timeout_seconds,
        echo=True,  #get_settings().database.database_echo
    )


sync_engine = _create_sync_engine()

SyncSessionLocal = sessionmaker(
    bind=sync_engine, 
    class_=Session, 
    autoflush=False, 
    autocommit=False, 
    expire_on_commit=False, 
    future=True)


@contextmanager
def get_session() -> Session:
    _sync_scoped_session: scoped_session = scoped_session(session_factory=SyncSessionLocal)
    try:
        yield _sync_scoped_session()
        _sync_scoped_session.commit()
    except Exception as ex:
        _sync_scoped_session.rollback()
        raise
    finally:
        _sync_scoped_session.remove()


@contextmanager
def get_connection():
    with sync_engine.connect() as connection:
        with connection.begin():
            yield connection

def run_migrations() -> None:
    with get_connection() as conn:
        with open('seeds/seed.sql') as file:
            conn.execute(text(file.read()))
