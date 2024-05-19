from typing import Any, List
from http import HTTPStatus
from bson import ObjectId

from fastapi import APIRouter, Depends, Body

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import UsuarioRepository
from src.schemas.usuario_schema import UsuarioPayload, ResponseUsuarioPayload, ResponsePagination
from src.schemas.base_schema import QueryPaginate

router = APIRouter(prefix='/usuario', tags=['Usuario'])


@router.get(
    path='/paginate', 
    status_code=HTTPStatus.OK,
    response_model=ResponsePagination, 
    summary='Pegar todos os Usuario'
)
def paginate(repository: UsuarioRepository = Depends()):
    return UsuarioService(repository).paginate()


@router.get(
    path='/{user_id}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario'
)
def get(user_id: str, repository: UsuarioRepository = Depends()):
    return UsuarioService(repository=repository).get_by_id(user_id)


@router.get(
    path='/cpf/{cpf}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario pelo CPF'
)
def get_by_cpf(cpf: str, repository: UsuarioRepository = Depends()) -> dict:
    return UsuarioService(repository=repository).get_by_cpf(cpf=cpf)


@router.post(
    path='/',
    status_code=HTTPStatus.CREATED,
    response_model=ResponseUsuarioPayload,
    summary='Criar Usuario'
)
def create(
    data: UsuarioPayload = Body(...), 
    repository: UsuarioRepository = Depends()
) -> dict[str, Any]:
    return UsuarioService(repository=repository).create(data=data)


@router.put(
    path='/{user_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseUsuarioPayload, 
    summary='Atualizar Usuario'
)
def update(
    user_id: str,
    data: UsuarioPayload, 
    repository: UsuarioRepository = Depends()
):
    return UsuarioService(repository=repository).update(user_id, data)


@router.delete(
    path='/{usuario_id}', 
    status_code=HTTPStatus.ACCEPTED,
    summary='Deletar Usuario'
)
def delete(usuario_id: str, repository: UsuarioRepository = Depends()):
    response = UsuarioService(repository=repository).delete(usuario_id)
    response['_id'] = str(response['_id'])
    return response
