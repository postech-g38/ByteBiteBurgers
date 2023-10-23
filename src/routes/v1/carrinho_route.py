from typing import Any

from fastapi import APIRouter, Depends

from src.services.carrinho_service import CarrinhoService
from src.adapters.repositories import EntityRepository
from src.schemas.carrinho_schema import CreateCarrinhoPayload, ResponseCarrinhoPayload

router = APIRouter(prefix='/carrinho', tags=['Carrinho'])


@router.get(
    path='/{id}', 
    response_model=ResponseCarrinhoPayload, 
    tags=['Pegar Carrinho']
)
def get(id: int, repository: EntityRepository = Depends()) -> ResponseCarrinhoPayload:
    service = CarrinhoService(repository=repository)
    return service.get(id=id)


@router.post(
    path='/', 
    response_model=ResponseCarrinhoPayload, 
    tags=['Criar Carrinho']
)
def create(data: CreateCarrinhoPayload, repository: EntityRepository = Depends()) -> ResponseCarrinhoPayload:
    service = CarrinhoService(repository=repository)
    return service.create(data=data)


@router.put(
    path='/', 
    response_model=ResponseCarrinhoPayload, 
    tags=['Atualizar Carrinho']
)
def update(data: CreateCarrinhoPayload, repository: EntityRepository = Depends()) -> ResponseCarrinhoPayload:
    service = CarrinhoService(repository=repository)
    return service.update(data=data)


@router.delete(
    path='/{id}', 
    response_model=ResponseCarrinhoPayload, 
    tags=['Deletar Carrinho']
)
def delete(id: int, repository: EntityRepository = Depends()) -> ResponseCarrinhoPayload:
    service = CarrinhoService(repository=repository)
    return service.delete(id=id)
