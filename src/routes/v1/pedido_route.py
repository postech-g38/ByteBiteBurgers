from fastapi import APIRouter, Depends, Response, Request

from src.services.pedido_service import PedidoService
from src.adapters.repositories import PedidoRepository
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, ResponsePagination
from src.schemas.base_schema import QueryPaginate

router = APIRouter(prefix='/pedido', tags=['Pedido'])


@router.get(
    path='/', 
    response_model=ResponsePagination, 
    summary='Pegar todos os Pedidos'
)
def get_all(query: QueryPaginate = Depends(), repository: PedidoRepository = Depends()):
    response = PedidoService(repository).get_all()
    return {
        'items': response,
        'quantidade': len(response)
    }


@router.get(
    path='/{pedido_id}', 
    response_model=ResponsePedidoPayload, 
    summary='Pegar Pedido'
)
def get(pedido_id: int, repository: PedidoRepository = Depends()):
    return PedidoService(repository).get_by_id(pedido_id)


@router.put(
    path='/{pedido_id}', 
    response_model=ResponsePedidoPayload, 
    summary='Atualizar Pedido'
)
def update(pedido_id: int, data: CreatePedidoPayload, repository: PedidoRepository = Depends()):
    return PedidoService(repository).update(pedido_id, data)


@router.delete(
    path='/{pedido_id}', 
    response_model=ResponsePedidoPayload, 
    summary='Deletar Pedido'
)
def delete(pedido_id: int, repository: PedidoRepository = Depends()):
    return PedidoService(repository).delete(pedido_id)


@router.get(
    path='/status', 
    response_model=ResponsePagination, 
    summary='Pegar Pedido por Status'
)
def pedido_get_by_status(status: str, repository: PedidoRepository = Depends()):
    return PedidoService(repository).get_by_status(status=status)


@router.get(
    path='/pendente', 
    response_model=ResponsePagination, 
    summary='Listagem de pedidos nao finalizados'
)
def pending_orders(repository: PedidoRepository = Depends()):
    return PedidoService(repository).pending_orders()


@router.post(
    path='/checkout', 
    response_model=ResponsePedidoPayload, 
    summary='Efetuar pagamento do Pedido'
)
def checkout(payload: CreatePedidoPayload, repository: PedidoRepository = Depends()):
    return PedidoService(repository).checkout(payload)
