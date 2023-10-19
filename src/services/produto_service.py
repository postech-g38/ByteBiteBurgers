import uuid

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.produto_model import ProdutoModel
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProdutoPayload, UpdateProdutoPayload


class ProdutoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> ResponseProdutoPayload:
        row = self.repository.produto.get_all()
        return ResponseProdutoPayload.model_validate(row).model_dump_json()
    
    def get(self, produto_id: int) -> ResponseProdutoPayload:
        row = self.repository.produto.search_by_id(model_id=produto_id)
        return ResponseProdutoPayload.model_validate(row).model_dump_json()
    
    def create(self, data: CreateProdutoPayload) -> ResponseProdutoPayload:
        row = ProdutoModel(**dict(data))
        row.id = uuid.uuid4().hex
        self.repository.produto.save(model=row)
        return ResponseProdutoPayload.model_validate(row).model_dump_json()

    def update(self, data: UpdateProdutoPayload) -> ResponseProdutoPayload:
        self.repository.produto.update(model_id=data.id, values=dict(data))
        row = self.repository.produto.search_by_id(model_id=data.id)
        return ResponseProdutoPayload.model_validate(row).model_dump_json()

    def delete(self, data: UpdateProdutoPayload) -> ResponseProdutoPayload:
        self.repository.produto.delete(model_id=data.id, values=dict(data))
        row = self.repository.produto.delete(model_id=data.id)
        return ResponseProdutoPayload.model_validate(row).model_dump_json()
    