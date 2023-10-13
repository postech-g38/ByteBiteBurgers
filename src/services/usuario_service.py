import uuid
from typing import List

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import CreateUsuarioPayload, ResponseUsuarioPayload, UpdateUsuarioPayload


class UsuarioService:
     def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
     def get_all(self) -> List[ResponseUsuarioPayload]:
        rows = self.repository.usuario.get_all()
        print("###########################")
        print("Resultados: " + str(len(rows)))
        print("###########################")
        return [ResponseUsuarioPayload.model_validate(row._asdict()) for row in rows]
    
     def get(self, id: int) -> ResponseUsuarioPayload:
        row = self.repository.usuario.search_by_id(model_id=id)
        return ResponseUsuarioPayload.model_validate(row).model_dump_json()
    
     def create(self, data: CreateUsuarioPayload) -> ResponseUsuarioPayload:
        row = UsuarioModel(**dict(data))
        row.id = uuid.uuid4().hex
        self.repository.user.save(model=row)
        return ResponseUsuarioPayload.model_validate(row).model_dump_json()

     def update(self, data: UpdateUsuarioPayload) -> ResponseUsuarioPayload:
        self.repository.usuario.update(model_id=data.id, values=dict(data))
        row = self.repository.usuario.search_by_id(model_id=data.id)
        return ResponseUsuarioPayload.model_validate(row).model_dump_json()

     def delete(self, id: int) -> ResponseUsuarioPayload:
        self.repository.usuario.delete(model_id=id)
        row = self.repository.usuario.delete(model_id=id)
        return ResponseUsuarioPayload.model_validate(row).model_dump_json()