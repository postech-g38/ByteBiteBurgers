from typing import Any, Dict, List, Optional, Type

from sqlalchemy import Select, asc, delete, desc, func, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.usuario_model import UsuarioModel


class UsuarioRepository(SQLAlchemyRepository):
     def __init__(self, database_session) -> None:
        super().__init__(session=database_session)
        self.entity_model = UsuarioModel

     def search_by_cpf(self, cpf: str) -> Type[UsuarioModel] | None:
        """Get item by cpf
        :param: cpf: ID of the model
        :return: UsuarioModel or None
        :raises ``sqlalchemy.repositories.exc.NoResultFound´´ or ``sqlalchemy.repositories.exc.MultipleResultsFound``
        """
        statement = select(self.entity_model).where(self.entity_model.cpf == cpf)
        results = self.session_db.execute(statement=statement)
        result = results.one_or_none()
        if result:
            (result,) = result
        return result
        