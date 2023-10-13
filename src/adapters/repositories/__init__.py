from fastapi import Depends
from sqlalchemy.orm.session import Session

from src.adapters.database import get_database_session
from src.adapters.repositories.usuario_repository import UsuarioRepository


class EntityRepository:
    def __init__(self, database: Session = Depends(get_database_session)) -> None:
        self.database = database
        self.usuario = UsuarioRepository(database_session=database)
        
