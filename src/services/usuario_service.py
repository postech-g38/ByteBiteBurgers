from typing import List
from datetime import datetime
from bson import ObjectId

from src.services.service_base import BaseService
from src.adapters.repositories import UsuarioRepository
from src.schemas.usuario_schema import UsuarioPayload, ResponseUsuarioPayload


class UsuarioService(BaseService):
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def paginate(self) -> List[ResponseUsuarioPayload]:
        data = self.query_result(self.repository.get_all())
        data = list(data)
        for i in data:
            i["id"] = str(i.pop("_id"))
        return{
            'items': data,
            'quantidade': len(data)
        }

    def get_by_id(self, user_id: int) -> ResponseUsuarioPayload:
        user_id = ObjectId(user_id)
        return self.query_result(self.repository.search_by_id(user_id))

    def get_by_cpf(self, cpf: str) -> ResponseUsuarioPayload:
        return self.query_result(self.repository.search_by_cpf(cpf))

    def create(self, data: UsuarioPayload) -> ResponseUsuarioPayload:
        data = data.model_dump()
        data.update({
            'created_at': datetime.now(),
            'updated_at': None,
            'deleted_at': None
        })
        usuario_id = self.repository.save(data)
        return self.repository.search_by_id(usuario_id)

    def update(self, user_id: int, data: UsuarioPayload) -> ResponseUsuarioPayload:
        user_id = ObjectId(user_id)
        data = data.model_dump()
        data['updated_at'] = datetime.now()
        self.query_result(self.repository.search_by_id(user_id))
        self.repository.update(user_id, data)
        row = self.repository.search_by_id(user_id)
        return row

    def delete(self, user_id: str) -> ResponseUsuarioPayload:
        user_id = ObjectId(user_id)
        row = self.query_result(self.repository.search_by_id(user_id))
        self.repository.delete(user_id)
        return row
    