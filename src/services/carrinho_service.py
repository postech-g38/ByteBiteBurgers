import uuid

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.carrinho_model import CarrinhoModel
from src.schemas.carrinho_schema import CreateCarrinhoPayload, ResponseCarrinhoPayload, UpdateCarrinhoPayload


class CarrinhoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> ResponseCarrinhoPayload:
        row = self.repository.carrinho.get_all()
        return ResponseCarrinhoPayload.model_validate(row).model_dump_json()
    
    def get(self, carrinho_id: int) -> ResponseCarrinhoPayload:
        row = self.repository.carrinho.search_by_id(model_id=carrinho_id)
        return ResponseCarrinhoPayload.model_validate(row).model_dump_json()
    
    def create(self, data: CreateCarrinhoPayload) -> ResponseCarrinhoPayload:
        row = CarrinhoModel(**dict(data))
        row.id = uuid.uuid4().hex
        self.repository.carrinho.save(model=row)
        return ResponseCarrinhoPayload.model_validate(row).model_dump_json()

    def update(self, data: UpdateCarrinhoPayload) -> ResponseCarrinhoPayload:
        self.repository.carrinho.update(model_id=data.id, values=dict(data))
        row = self.repository.carrinho.search_by_id(model_id=data.id)
        return ResponseCarrinhoPayload.model_validate(row).model_dump_json()

    def delete(self, data: UpdateCarrinhoPayload) -> ResponseCarrinhoPayload:
        self.repository.carrinho.delete(model_id=data.id, values=dict(data))
        row = self.repository.carrinho.delete(model_id=data.id)
        return ResponseCarrinhoPayload.model_validate(row).model_dump_json()