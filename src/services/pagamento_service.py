from fastapi import Response

from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.database.models.pagamento_model import PagamentoModel

class PagamentoService:
    def __init__(self, repository: PagamentoRepository) -> None:
        self.repository = repository
    
    def create(self, data: PagamentoPayloadSchema) -> Response:
        return self.repository.save(PagamentoModel(**data.model_dump()))
    
    def get_by_pedido_id(self, pedido_id: int) -> Response:
        row = self.repository.pedido.search_by_id(model_id=pedido_id)
        return {'status_pagamento': row.status_pagamento}

    def payment_response(self, payload) -> dict:
        return {'status': 'ok'}
    