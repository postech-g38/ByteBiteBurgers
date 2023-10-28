from typing import Any

from fastapi import APIRouter, Depends
from starlette import status

from src.services.pedido_service import PedidoService
from src.adapters.repositories import EntityRepository
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, ResponsePagination
from src.schemas.checkout_schema import CreateCheckoutPayload, ResponseCheckoutPayload

router = APIRouter(prefix='/pedido', tags=['Pedido'])


@router.get(
    path='/', 
    response_model=ResponsePagination, 
    summary='Pegar todos os Pedidos'
)
def get_all(repository: EntityRepository = Depends()) -> dict:
    return PedidoService(repository=repository).get_all()


@router.get(
    path='/{id}', 
    response_model=ResponsePedidoPayload, 
    summary='Pegar Pedido'
)
def get(id: int, repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.get(id=id)


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponsePedidoPayload, 
    summary='Criar Pedido'
)
def create(data: CreatePedidoPayload, repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.create(data=data)


@router.put(
    path='/', 
    response_model=ResponsePedidoPayload, 
    summary='Atualizar Pedido'
)
def update(data: CreatePedidoPayload, repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.update(data=data)


@router.delete(
    path='/{id}', 
    response_model=ResponsePedidoPayload, 
    summary='Deletar Pedido'
)
def delete(id: int, repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.delete(id=id)


@router.post(
    path='/checkout', 
    response_model=ResponseCheckoutPayload, 
    summary='Efetuar pagamento do Pedido'
)
def checkout(payload: CreateCheckoutPayload, repository: EntityRepository = Depends()) -> dict:
    return PedidoService(repository=repository).chekout(payload=payload)
