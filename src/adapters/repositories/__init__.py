from fastapi import Depends
from sqlalchemy.orm.session import Session

from src.adapters.database import get_database_session


class EntityRepository:
    def __init__(self, session_db: Session = Depends(get_database_session)) -> None:
        self.repository_name = ''
