import uuid
from typing import List

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.produto_model import ProdutoModel
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProdutoPayload, UpdateProdutoPayload


class ProdutoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> List[ResponseProdutoPayload]:
        rows = self.repository.produto.get_all()
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
        row = self.repository.produto.search_by_id(model_id=id)
        if not row:
            return None
        return row.__dict__
    
    def create(self, data: CreateProdutoPayload) -> dict | None:
        row = ProdutoModel(**dict(data))
        self.repository.produto.save(model=row)
        return row

    def update(self, data: UpdateProdutoPayload) -> dict | None:
        self.repository.produto.update(model=data, values=dict(data))
        row = self.repository.produto.search_by_id(model_id=data.id)
        return row

    def delete(self, id: int) -> int:
        row = self.repository.produto.delete(model_id=id)
        return id