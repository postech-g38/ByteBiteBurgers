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
        print(rows)
        if not rows:
            return {
                'items': [],
                'quantidade': 0
            }
        
        rows = [i.__dict__ for (i, )in rows]
        [i.pop('_sa_instance_state') for i in rows]
      
        return {
            'items': rows,
            'quantidade': len(rows)
        }
     
    def get(self, id: int) -> dict | None:
        row = self.repository.usuario.search_by_id(model_id=id)
        if not row:
            return None
        return row.__dict__
    
    def create(self, data: CreateUsuarioPayload) -> dict | None:
        row = UsuarioModel(**dict(data))
        self.repository.usuario.save(model=row)
        return row

    def update(self, data: UpdateUsuarioPayload) -> dict | None:
        self.repository.usuario.update(model=data, values=dict(data))
        row = self.repository.usuario.search_by_id(model_id=data.id)
        return row

    def delete(self, id: int) -> int:
        row = self.repository.usuario.delete(model_id=id)
        return id