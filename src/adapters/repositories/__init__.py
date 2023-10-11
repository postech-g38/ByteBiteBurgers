from fastapi import Depends
from sqlalchemy.orm.session import Session

from src.adapters.database import get_database_session
from src.adapters.repositories.user_repository import UsuarioRepositorio


class EntityRepository:
    def __init__(self, database: Session = Depends(get_database_session)) -> None:
        self.database = database
        self.usuario = UsuarioRepositorio(database_session=database)
        
