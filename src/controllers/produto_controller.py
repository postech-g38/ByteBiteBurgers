from typing import Any
from datetime import datetime

from src.controllers.base_controller import BaseController
from src.adapters.repositories import EntityRepository
from src.adapters.database.models.produto_model import ProdutoModel
from src.presenters.produto_schema import CreateProdutoPayload, ResponseProdutoPayload, UpdateProdutoPayload


class ProdutoController(BaseController):
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> dict[str, Any]:
        rows = self.query_result(result=self.repository.produto.get_all())
        rows = [ResponseProdutoPayload.model_validate(i).model_dump() for i in rows]
        return {
            'items': rows,
            'quantidade': len(rows)
        }

    def get(self, id: str):
        row = self.query_result(self.repository.produto.search_by_id(model_id=id))
        return ResponseProdutoPayload.model_validate(row).model_dump()
        
    def create(self, data: CreateProdutoPayload) -> dict[str, Any]:
        row = ProdutoModel(**data.model_dump())
        row = self.repository.produto.save(model=row)
        return ResponseProdutoPayload.model_validate(row).model_dump() 
    
    def update(self, data: UpdateProdutoPayload) -> dict[str, Any]:
        row = self.query_result(self.repository.produto.search_by_id(model_id=data.id))
        self.repository.produto.update(model_id=data.id, values=data.model_dump())
        row = self.repository.produto.model_refresh(model=row)
        return ResponseProdutoPayload.model_validate(row).model_dump()
    
    def delete(self, id: str | int) -> dict[str, Any]:
        row = self.query_result(self.repository.produto.search_by_id(model_id=id))
        row.deleted_at = datetime.now()
        self.repository.produto.delete(model_id=id)
        return ResponseProdutoPayload.model_validate(row).model_dump()
    
    def get_by_categoria(self, categoria: str):  #  -> dict[str, Any]
        categoria = categoria.title()
        rows = self.query_result(self.repository.produto.get_by_categoria(categoria=categoria))
        rows = [ResponseProdutoPayload.model_validate(i).model_dump() for i in rows]
        return {
            'items': rows,
            'quantidade': len(rows)
        }