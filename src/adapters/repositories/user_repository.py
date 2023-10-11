from typing import Any, Dict, List, Optional, Type

from sqlalchemy import Select, asc, delete, desc, func, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models import UsuarioModel


class UsuarioRepositorio(SQLAlchemyRepository):
    def __init__(self, database_session) -> None:
        super().__init__(session=database_session)
        self.entity_model = UsuarioModel
        