from typing import List
from datetime import datetime

from src.services.service_base import BaseService
from src.adapters.repositories import UsuarioRepository
from src.adapters.database.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import UsuarioPayload, ResponseUsuarioPayload


class UsuarioService(BaseService):
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository
    
    def paginate(self, query) -> List[UsuarioModel]:
        return self.query_result(result=self.repository.get_all())
     
    def get_by_id(self, user_id: int) -> UsuarioModel:
        return self.query_result(self.repository.search_by_id(user_id))
     
    def get_by_cpf(self, cpf: str) -> UsuarioModel:
        return self.query_result(self.repository.search_by_cpf(cpf))
    
    def create(self, data: UsuarioPayload) -> UsuarioModel:
        data = self.repository.save(UsuarioModel(**data.model_dump()))
        return data

    def update(self, user_id: int, data: UsuarioPayload) -> UsuarioModel:
        self.query_result(self.repository.search_by_id(user_id))
        self.repository.update(user_id, data)
        row = self.repository.search_by_id(user_id)
        return row

    def delete(self, user_id: str, hard_delete: bool = False) -> UsuarioModel:
        row = self.query_result(self.repository.search_by_id(user_id))
        row.deleted_at = datetime.now()
        self.repository.delete(user_id)
        return row
    