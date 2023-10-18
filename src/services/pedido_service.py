import uuid

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, UpdatePedidoPayload


class PedidoService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> ResponsePedidoPayload:
        row = self.repository.pedido.get_all()
        return ResponsePedidoPayload.model_validate(row).model_dump_json()
    
    def get(self, pedido_id: int) -> ResponsePedidoPayload:
        row = self.repository.pedido.search_by_id(model_id=pedido_id)
        return ResponsePedidoPayload.model_validate(row).model_dump_json()
    
    def create(self, data: CreatePedidoPayload) -> ResponsePedidoPayload:
        row = PedidoModel(**dict(data))
        row.id = uuid.uuid4().hex
        self.repository.pedido.save(model=row)
        return ResponsePedidoPayload.model_validate(row).model_dump_json()

    def update(self, data: UpdatePedidoPayload) -> ResponsePedidoPayload:
        self.repository.pedido.update(model_id=data.id, values=dict(data))
        row = self.repository.pedido.search_by_id(model_id=data.id)
        return ResponsePedidoPayload.model_validate(row).model_dump_json()

    def delete(self, data: UpdatePedidoPayload) -> ResponsePedidoPayload:
        self.repository.pedido.delete(model_id=data.id, values=dict(data))
        row = self.repository.pedido.delete(model_id=data.id)
        return ResponsePedidoPayload.model_validate(row).model_dump_json()
    