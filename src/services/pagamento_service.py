from http import HTTPStatus
from typing import Dict, Any

from fastapi import Response

from src.services.service_base import BaseService
from src.schemas.pagamento_schema import (
    PagamentoPayloadSchema, 
    PagamentoResponseSchema, 
    PagamentoWebhookSchema, 
    PagamentoWebhookResponse
)
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.api.bytebiteburgers.settings import ByteBiteBurguers
from src.adapters.database.models.pagamento_model import PagamentoModel


class PagamentoService(BaseService):
    def __init__(self, repository: PagamentoRepository, orders: ByteBiteBurguers) -> None:
        self._repository = repository
        self._orders = orders

    def create(self, data: PagamentoPayloadSchema) -> Dict[str, Any]:
        pagamento = self._repository.save(PagamentoModel(**data.model_dump()))
        return PagamentoResponseSchema.model_validate(pagamento).model_dump()
    
    def get_by_pedido_id(self, pedido_id: int) -> Dict[str, Any]:
        pagamento = self.query_result(self._repository.get_by_pedido_id(pedido_id))
        return PagamentoResponseSchema.model_validate(pagamento).model_dump(),
    
    def update_status(self, payload: PagamentoWebhookSchema) -> Dict[str, Any]:
        pagamento = self._repository.search_by_id(payload.pagamento_id)
        self._repository.update(payload.pagamento_id, {'status': payload.pagamento_status})
        self._orders.update_pedido(pagamento.pedido_id, {'status': payload.pagamento_status})
        return PagamentoResponseSchema.model_validate(pagamento).model_dump(),
    