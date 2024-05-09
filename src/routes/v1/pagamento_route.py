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
    summary='Pegar Pagamento por um Pedido ID'
)
def get_order_payment_status(pedido_id: int, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository).get_by_pedido_id(pedido_id)


@router.post(
    path='/webhook', 
    summary='Webhook para atualizaçao do status do Pagamento'
)
def get_order_payment_status(data: PagamentoWebhookSchema, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository).payment_response(data)
