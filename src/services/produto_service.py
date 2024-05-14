from typing import Any, List
from datetime import datetime

from src.services.service_base import BaseService
from src.adapters.repositories import ProdutoRepository
from src.adapters.database.models.produto_model import ProdutoModel
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProduto


class ProdutoService(BaseService):
    def __init__(self, repository: ProdutoRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> List[ProdutoModel]:
        return self.query_result(self.repository.get_all())

    def get_by_id(self, produto_id: int) -> ProdutoModel:
        return self.query_result(self.repository.search_by_id(produto_id))
        
    def create(self, data: CreateProdutoPayload) -> ProdutoModel:
        return self.repository.save(ProdutoModel(**data.model_dump()))
    
    def update(self, produto_id: int, data: CreateProdutoPayload) -> ProdutoModel:
        self.repository.update(produto_id, data.model_dump())
        return self.query_result(self.repository.search_by_id(produto_id))
    
    def delete(self, produto_id: int) -> ProdutoModel:
        data = self.query_result(self.repository.search_by_id(produto_id))
        data.deleted_at = datetime.now()
        self.repository.delete(produto_id)
        return data
    
    def get_by_categoria(self, categoria: str) -> List[ProdutoModel]:
        return self.query_result(self.repository.get_by_categoria(categoria.title()))
