
from fastapi import APIRouter, Depends, Request

from src.services.pedido_service import PedidoService
from src.adapters.repositories import PedidoRepository
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, ResponsePagination, UpdatePedidoPayload


router = APIRouter(prefix='/pedido', tags=['Pedido'])

@router.get(
    path='/pendente', 
    response_model=ResponsePagination, 
    summary='Listagem de pedidos nao finalizados'
)
def pending_orders(request: Request, repository: PedidoRepository = Depends()) -> dict:
    pedido = PedidoService(repository=repository).pending_orders()
    print(pedido)
    return pedido


@router.get(
    path='/', 
    response_model=ResponsePagination, 
    summary='Pegar todos os Pedidos'
)
def get_all(request: Request, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).get_all()


@router.get(
    path='/status', 
    response_model=ResponsePagination, 
    summary='Pegar Pedido por Status'
)
def pedido_get_by_status(status: str, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).get_by_status(status=status)


@router.get(
    path='/{id}', 
    response_model=ResponsePedidoPayload, 
    summary='Pegar Pedido'
)
def get(id: int, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).get_by_id(id=id)


@router.put(
    path='/', 
    response_model=ResponsePedidoPayload, 
    summary='Atualizar Pedido'
)
def update(data: UpdatePedidoPayload, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).update(data=data)


@router.delete(
    path='/{id}', 
    response_model=ResponsePedidoPayload, 
    summary='Deletar Pedido'
)
def delete(id: int, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).delete(id=id)


@router.post(
    path='/checkout', 
    response_model=ResponsePedidoPayload, 
    summary='Efetuar pagamento do Pedido'
)
def checkout(payload: CreatePedidoPayload, repository: PedidoRepository = Depends()) -> dict:
    return PedidoService(repository=repository).checkout(data=payload)
