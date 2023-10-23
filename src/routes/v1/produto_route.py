from typing import Any

from fastapi import APIRouter, Depends

from src.services.produto_service import ProdutoService
from src.adapters.repositories import EntityRepository
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProdutoPayload

router = APIRouter(prefix='/produto', tags=['Produto'])


@router.get(
    path='/', 
    # response_model=ResponseProdutoPayload, 
    tags=['Pegar todos os Produtos']
)
def get_all(repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.get_all()


@router.get(
    path='/{id}', 
    response_model=ResponseProdutoPayload, 
    tags=['Pegar Produto']
)
def get(id: int, repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.get(id=id)


@router.post(
    path='/', 
    response_model=ResponseProdutoPayload, 
    tags=['Criar Produto']
)
def create(data: CreateProdutoPayload, repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.create(data=data)


@router.put(
    path='/', 
    response_model=ResponseProdutoPayload, 
    tags=['Atualizar Produto']
)
def update(data: CreateProdutoPayload, repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.update(data=data)


@router.delete(
    path='/{id}', 
    response_model=int, 
    tags=['Deletar Produto']
)
def delete(id: int, repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.delete(id=id)
