from typing import Any
import uuid

from src.adapters.repositories import EntityRepository
from src.adapters.database.models import UsuarioModel
from src.schemas.user_schema import CreateUserPayload, ResponseUserPayload, UpdateUserPayload


class UsuarioService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_user(self, user_id: int) -> ResponseUserPayload:
        row = self.repository.usuario.search_by_id(model_id=user_id)
        return ResponseUserPayload.model_validate(row).model_dump_json()
    
    def create_user(self, data: CreateUserPayload) -> ResponseUserPayload:
        row = UsuarioModel(**dict(data))
        row.id = uuid.uuid4().hex
        self.repository.user.save(model=row)
        return ResponseUserPayload.model_validate(row).model_dump_json()

    def update_user(self, data: UpdateUserPayload) -> ResponseUserPayload:
        self.repository.usuario.update(model_id=data.id, values=dict(data))
        row = self.repository.usuario.search_by_id(model_id=data.id)
        return ResponseUserPayload.model_validate(row).model_dump_json()