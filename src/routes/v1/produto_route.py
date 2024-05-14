from typing import Any

from fastapi import APIRouter, Depends
from http import HTTPStatus

from src.services.produto_service import ProdutoService
from src.adapters.repositories import ProdutoRepository
from src.schemas.produto_schema import CreateProdutoPayload, ResponseProduto, ResponsePagination

router = APIRouter(prefix='/produto', tags=['Produto'])


@router.get(
    path='/', 
    status_code=HTTPStatus.OK,
    response_model=ResponsePagination, 
    summary='Pegar todos os Produtos'
)
def paginate(repository: ProdutoRepository = Depends()):
    response = ProdutoService(repository).get_all()
    return {
        'items': response,
        'quantidade': len(response)
    }


@router.get(
    path='/{produto_id}',
    status_code=HTTPStatus.OK,
    response_model=ResponseProduto, 
    summary='Pegar Produto'
)
def get(produto_id: int, repository: ProdutoRepository = Depends()):
    return ProdutoService(repository).get_by_id(produto_id)


@router.post(
    path='/', 
    status_code=HTTPStatus.CREATED,
    response_model=ResponseProduto, 
    summary='Criar Produto'
)
def create(data: CreateProdutoPayload, repository: ProdutoRepository = Depends()):
    return ProdutoService(repository).create(data=data)


@router.put(
    path='/{produto_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProduto, 
    summary='Atualizar Produto'
)
def update(produto_id: int, data: CreateProdutoPayload, repository: ProdutoRepository = Depends()):
    return ProdutoService(repository).update(produto_id, data)


@router.delete(
    path='/{produto_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseProduto, 
    summary='Deletar Produto'
)
def delete(produto_id: int, repository: ProdutoRepository = Depends()):
    return ProdutoService(repository).delete(produto_id)


@router.get(
    path='/categoria', 
    status_code=HTTPStatus.OK,
    response_model=ResponsePagination, 
    summary='Pegar Produtos por Categoria'
)
def get_by_category(categoria: str, repository: ProdutoRepository = Depends()):
    return ProdutoService(repository).get_by_categoria(categoria=categoria)
