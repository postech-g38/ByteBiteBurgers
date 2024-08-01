from http import HTTPStatus

from fastapi import APIRouter, Depends, Path, Body
from fastapi.responses import JSONResponse

from src.services.pagamento_service import PagamentoService
from src.schemas.pagamento_schema import PagamentoPayloadSchema, PagamentoWebhookSchema
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.api import ByteBiteBurguers, bytebiteburguers_facade
from src.constants import HEADERS

router = APIRouter()


@router.post(
    path='/',
    summary='Criar um Pagamento'
)
def create_payment(
    data: PagamentoPayloadSchema = Body(), 
    repository: PagamentoRepository = Depends(),
    orders: ByteBiteBurguers = Depends(bytebiteburguers_facade)
):
    data = PagamentoService(repository, orders).create(data)
    return JSONResponse(
        status_code=HTTPStatus.CREATED,
        headers=HEADERS,
        content=data,
        
    )


@router.get(
    path='/pedido/{pedido_id}', 
    summary='Pegar Pagamento por um Pedido ID'
)
def get_order_payment_status(
    pedido_id: int = Path(...), 
    repository: PagamentoRepository = Depends(),
    orders: ByteBiteBurguers = Depends(bytebiteburguers_facade)
):
    data = PagamentoService(repository, orders).get_by_pedido_id(pedido_id)
    return JSONResponse(
        status_code=HTTPStatus.OK,
        headers=HEADERS,
        content=data,
    )


@router.post(
    path='/pagamento/webhook', 
    summary='Pegar Pagamento por um Pedido ID'
)
def update_payment_status(
    payload: PagamentoWebhookSchema = Body(...), 
    repository: PagamentoRepository = Depends(),
    orders: ByteBiteBurguers = Depends(bytebiteburguers_facade)
):
    data = PagamentoService(repository, orders).update_status(payload)
    return JSONResponse(
        status_code=HTTPStatus.OK,
        headers=HEADERS,
        content=data,
    )
