from typing import Any, List
from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import UsuarioRepository
from src.schemas.usuario_schema import UsuarioPayload, ResponseUsuarioPayload
from src.schemas.base_schema import QueryPaginate

router = APIRouter(prefix='/usuario', tags=['Usuario'])


@router.get(
    path='/paginate', 
    status_code=HTTPStatus.OK,
    # response_model=ResponsePagination, 
    summary='Pegar todos os Usuario'
)
def paginate(repository: UsuarioRepository = Depends()):
    return UsuarioService(repository=repository).paginate()


@router.get(
    path='/{user_id}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario'
)
def get(user_id: int, repository: UsuarioRepository = Depends()):
    service = UsuarioService(repository=repository)
    return service.get_by_id(user_id)


@router.get(
    path='/cpf/{cpf}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario pelo CPF'
)
def get(cpf: str, repository: UsuarioRepository = Depends()) -> dict:
    service = UsuarioService(repository=repository)
    return service.get_by_cpf(cpf=cpf)


@router.post(
    path='/',
    status_code=HTTPStatus.CREATED,
    response_model=ResponseUsuarioPayload,
    summary='Criar Usuario'
)
def create(
    data: UsuarioPayload, 
    repository: UsuarioRepository = Depends()
) -> dict[str, Any]:
    service = UsuarioService(repository=repository)
    return service.create(data=data)


@router.put(
    path='/{user_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseUsuarioPayload, 
    summary='Atualizar Usuario'
)
def update(
    user_id: int,
    data: UsuarioPayload, 
    repository: UsuarioRepository = Depends()
):
    service = UsuarioService(repository=repository)
    return service.update(user_id, data)


@router.delete(
    path='/{id}', 
    status_code=HTTPStatus.ACCEPTED,
    summary='Deletar Usuario'
)
def delete(id: str, repository: UsuarioRepository = Depends()):
    return UsuarioService(repository=repository).delete(id=id)
