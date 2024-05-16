from fastapi import APIRouter, Depends

<<<<<<< HEAD
from src.services.pagamento_service import PagamentoService
from src.schemas.pagamento_schema import PagamentoWebhookSchema
from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.adapters.repositories.pagamento_repository import PagamentoRepository

router = APIRouter()
=======
from src.services.pagamento_service import PagamentoController
from src.adapters.repositories import EntityRepository
from src.presenters.pagamento_schema import PagamentoWebhookSchema
>>>>>>> main


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
<<<<<<< HEAD
def get_order_payment_status(pedido_id: int, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository).get_by_pedido_id(pedido_id)
=======
def get_order_payment_status(pedido_id: int, repository: EntityRepository = Depends()) -> dict:
    return PagamentoController(repository=repository).get_pedido_status(pedido_id=pedido_id)
>>>>>>> main


@router.post(
    path='/webhook', 
    summary='Webhook para atualizaçao do status do Pagamento'
)
<<<<<<< HEAD
def get_order_payment_status(data: PagamentoWebhookSchema, repository: PagamentoRepository = Depends()):
    return PagamentoService(repository).payment_response(data)
=======
def get_order_payment_status(data: PagamentoWebhookSchema, repository: EntityRepository = Depends()) -> dict:
    return PagamentoController(repository=repository).payment_response(payload=data)
>>>>>>> main
