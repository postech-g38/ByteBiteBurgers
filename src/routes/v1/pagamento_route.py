from fastapi import APIRouter, Depends

from src.services.pagamento_service import PagamentoService
from src.schemas.pagamento_schema import PagamentoWebhookSchema
from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.adapters.repositories.pagamento_repository import PagamentoRepository

router = APIRouter()


@router.post(
    path='/',
    summary='Criar um Pagamento'
)
def create_payment(data: PagamentoPayloadSchema, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository).create(data)


@router.get(
    path='/pedido/{pedido_id}', 
    summary='Pegar status do pagamento por um Pedido ID'
)
def get_order_payment_status(pedido_id: int, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository=repository).get_by_pedido_id(pedido_id)


@router.post(
    path='/webhook', 
    # response_model=ResponsePagination, 
    summary='Webhook para atualizaçao do status do pagamento'
)
def get_order_payment_status(data: PagamentoWebhookSchema, repository) -> dict:
    return PagamentoService(repository=repository).payment_response(payload=data)
