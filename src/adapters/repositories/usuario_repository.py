from typing import Dict, Any

from fastapi import Depends

from src.adapters.repositories.mongodb_repository import PyMongoRepository
from src.adapters.database import get_database_session


class UsuarioRepository(PyMongoRepository):
	def __init__(self, database_session=Depends(get_database_session)) -> None:
		super().__init__(database_session, 'mongo', 'usuarios')

	def search_by_cpf(self, cpf: str) -> Dict[str, Any] | None:
		return self._collection.find_one({'cpf': cpf}, session=self._session)
        