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
    summary='Pegar todos os Produtos'
)
def get_all(repository: EntityRepository = Depends()) -> dict:
    return ProdutoService(repository=repository).get_all()


@router.get(
    path='/categoria', 
    status_code=HTTPStatus.OK,
    response_model=ResponsePagination, 
    summary='Pegar Produtos por Categoria'
)
def get_by_category(categoria: str, repository: EntityRepository = Depends()) -> dict:
    return ProdutoService(repository=repository).get_by_categoria(categoria=categoria)


@router.get(
    path='/{id}',
    status_code=HTTPStatus.OK,
    response_model=ResponseProdutoPayload, 
    summary='Pegar Produto'
)
def get(id: int | str, repository: EntityRepository = Depends()) -> dict:
    return ProdutoService(repository=repository).get(id=id)


@router.post(
    path='/', 
    status_code=HTTPStatus.CREATED,
    response_model=ResponseProdutoPayload, 
    summary='Criar Produto'
)
def create(data: CreateProdutoPayload, repository: EntityRepository = Depends()) -> dict:
    return ProdutoService(repository=repository).create(data=data)


@router.put(
    path='/',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProdutoPayload, 
    summary='Atualizar Produto'
)
def update(data: UpdateProdutoPayload, repository: EntityRepository = Depends()) -> dict:
    return ProdutoService(repository=repository).update(data=data)


@router.delete(
    path='/{id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProdutoPayload, 
    summary='Deletar Produto'
)
def delete(id: int | str, repository: EntityRepository = Depends()) -> dict:
    service = ProdutoService(repository=repository)
    return service.delete(id=id)
