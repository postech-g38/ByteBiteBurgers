import uuid
from typing import List

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.carrinho_model import CarrinhoModel
from src.schemas.carrinho_schema import CreateCarrinhoPayload, ResponseCarrinhoPayload, UpdateCarrinhoPayload


class CarrinhoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> List[ResponseCarrinhoPayload]:
        rows = self.repository.carrinho.get_all()
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
        row = self.repository.carrinho.search_by_id(model_id=id)
        if not row:
            return None
        return row.__dict__
    
    def create(self, data: CreateCarrinhoPayload) -> dict | None:
        row = CarrinhoModel(**dict(data))
        self.repository.carrinho.save(model=row)
        return row

    def update(self, data: UpdateCarrinhoPayload) -> dict | None:
        self.repository.carrinho.update(model=data, values=dict(data))
        row = self.repository.carrinho.search_by_id(model_id=data.id)
        return row

    def delete(self, id: int) -> int:
        row = self.repository.carrinho.delete(model_id=id)
        return id