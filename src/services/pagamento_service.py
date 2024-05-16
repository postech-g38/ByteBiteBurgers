from http import HTTPStatus

from fastapi import Response

from src.services.service_base import BaseService
from src.schemas.pagamento_schema import (
    PagamentoPayloadSchema, 
    PagamentoResponseSchema, 
    PagamentoWebhookSchema, 
    PagamentoWebhookResponse
)
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.database.models.pagamento_model import PagamentoModel


class PagamentoService(BaseService):
    def __init__(self, repository: PagamentoRepository) -> None:
        self.repository = repository
    
    def create(self, data: PagamentoPayloadSchema) -> Response:
        pagamento = self.repository.save(PagamentoModel(**data.model_dump()))
        return Response(
            PagamentoResponseSchema.model_validate(pagamento).model_dump_json(), 
            HTTPStatus.CREATED
        )
    
    def get_by_pedido_id(self, pedido_id: int) -> Response:
        pagamento = self.query_result(self.repository.get_by_pedido_id(pedido_id))
        return Response(
            PagamentoResponseSchema.model_validate(pagamento).model_dump_json(), 
            HTTPStatus.OK
        )
    