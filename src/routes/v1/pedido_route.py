from typing import Any

from fastapi import APIRouter, Depends

from src.services.pedido_service import PedidoService
from src.adapters.repositories import EntityRepository
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload

router = APIRouter(prefix='/pedido', tags=['Pedido'])


@router.get(
    path='/', 
    # response_model=ResponsePedidoPayload, 
    summary='Pegar todos os Pedidos'
)
def get_all(repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.get_all()


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


# TODO verificar se será necessário este endpoint, e se está no arquivo correto
@router.post(
    path='/checkout', 
    response_model=ResponsePedidoPayload, 
    summary='Efetuar pagamento do Pedido'
)
def create(data: CreatePedidoPayload, repository: EntityRepository = Depends()) -> dict:
    service = PedidoService(repository=repository)
    return service.create(data=data)
