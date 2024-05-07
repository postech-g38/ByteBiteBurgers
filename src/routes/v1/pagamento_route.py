
from fastapi import APIRouter, Depends

from src.controllers.pagamento_controller import PagamentoController
from src.adapters.repositories import EntityRepository
from src.presenters.pagamento_schema import PagamentoWebhookSchema


router = APIRouter(prefix='/pagamento', tags=['Pedido'])


@router.get(
    path='/pedido/{pedido_id}', 
    # response_model=ResponsePagination, 
    summary='Pegar status do pagamento de um Pedido ID'
)
def get_order_payment_status(pedido_id: int, repository: EntityRepository = Depends()) -> dict:
    return PagamentoController(repository=repository).get_pedido_status(pedido_id=pedido_id)


@router.post(
    path='/webhook', 
    # response_model=ResponsePagination, 
    summary='Webhook para atualizaçao do status do pagamento'
)
def get_order_payment_status(data: PagamentoWebhookSchema, repository: EntityRepository = Depends()) -> dict:
    return PagamentoController(repository=repository).payment_response(payload=data)
