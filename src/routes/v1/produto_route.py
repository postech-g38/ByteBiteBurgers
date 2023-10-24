from typing import Any

from fastapi import APIRouter, Depends
from http import HTTPStatus

from src.services.produto_service import ProdutoService
from src.adapters.repositories import EntityRepository
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProdutoPayload, ResponsePagination, UpdateProdutoPayload

router = APIRouter(prefix='/produto', tags=['Produto'])


@router.get(
    path='/', 
    status_code=HTTPStatus.OK,
    response_model=ResponsePagination, 
    tags=['Pegar todos os Produtos']
)
def get_all(repository: EntityRepository = Depends()) -> ResponsePagination:
    return ProdutoService(repository=repository).get_all()


@router.get(
    path='/{id}',
    status_code=HTTPStatus.OK,
    response_model=ResponseProdutoPayload, 
    tags=['Pegar Produto']
)
def get(id: int | str, repository: EntityRepository = Depends()) -> ResponseProdutoPayload:
    return ProdutoService(repository=repository).get(id=id)


@router.post(
    path='/criar', 
    status_code=HTTPStatus.CREATED,
    response_model=ResponseProdutoPayload, 
    tags=['Criar Produto']
)
def create(
    data: CreateProdutoPayload,
    repository: EntityRepository = Depends()
) -> ResponseProdutoPayload:
    return ProdutoService(repository=repository).create(data=data)


@router.put(
    path='/atualizar', 
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProdutoPayload, 
    tags=['Atualizar Produto']
)
def update(
    data: UpdateProdutoPayload, 
    repository: EntityRepository = Depends()
) -> ResponseProdutoPayload:
    print(data)
    return ProdutoService(repository=repository).update(data=data)


@router.delete(
    path='/{id}', 
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProdutoPayload, 
    tags=['Deletar Produto']
)
def delete(id: int | str, repository: EntityRepository = Depends()) -> ResponseProdutoPayload:
    return ProdutoService(repository=repository).delete(id=id)
