from typing import List

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, UpdatePedidoPayload


class PedidoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> List[ResponsePedidoPayload]:
        rows = self.repository.pedido.get_all()
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
        row = self.repository.pedido.search_by_id(model_id=id)
        if not row:
            return None
        return row.__dict__
    
    def create(self, data: CreatePedidoPayload) -> dict | None:
        row = PedidoModel(**dict(data))
        self.repository.pedido.save(model=row)
        return row

    def update(self, data: UpdatePedidoPayload) -> dict | None:
        self.repository.pedido.update(model=data, values=dict(data))
        row = self.repository.pedido.search_by_id(model_id=data.id)
        return row

    def delete(self, id: int) -> int:
        row = self.repository.pedido.delete(model_id=id)
        return id