from typing import Any, List
from http import HTTPStatus

from fastapi import APIRouter, Depends

<<<<<<< HEAD
from src.services.usuario_service import UsuarioService
from src.adapters.database import get_database_session
from src.adapters.repositories import UsuarioRepository
from src.schemas.usuario_schema import UsuarioPayload, ResponseUsuarioPayload, ResponsePagination
from src.schemas.base_schema import QueryPaginate
=======
from src.controllers.usuario_controller import UsuarioController
from src.adapters.repositories import EntityRepository
from src.presenters.usuario_schema import CreateUsuarioPayload, ResponseUsuarioPayload, ResponsePagination, UpdateUsuarioPayload
>>>>>>> main

router = APIRouter(prefix='/usuario', tags=['Usuario'])


@router.get(
    path='/paginate', 
    status_code=HTTPStatus.OK,
    # response_model=ResponsePagination, 
    summary='Pegar todos os Usuario'
)
<<<<<<< HEAD
def paginate(query: QueryPaginate, repository: UsuarioRepository = Depends()):
    return UsuarioService(repository=repository).paginate(query)
=======
def get_all(repository: EntityRepository = Depends()) -> ResponsePagination:
    return UsuarioController(repository=repository).get_all()
>>>>>>> main


@router.get(
    path='/{user_id}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario'
)
<<<<<<< HEAD
def get(user_id: int, repository: UsuarioRepository = Depends()):
    service = UsuarioService(repository=repository)
    return service.get_by_id(user_id)
=======
def get(id: int | str, repository: EntityRepository = Depends()):
    service = UsuarioController(repository=repository)
    return service.get_by_id(id=id)
>>>>>>> main


@router.get(
    path='/cpf/{cpf}', 
    status_code=HTTPStatus.OK,
    response_model=ResponseUsuarioPayload, 
    summary='Pegar Usuario pelo CPF'
)
<<<<<<< HEAD
def get(cpf: str, repository: UsuarioRepository = Depends()) -> dict:
    service = UsuarioService(repository=repository)
=======
def get(cpf: str, repository: EntityRepository = Depends()) -> dict:
    service = UsuarioController(repository=repository)
>>>>>>> main
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
    service = UsuarioController(repository=repository)
    return service.create(data=data)


@router.put(
    path='/{user_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=ResponseUsuarioPayload, 
    summary='Atualizar Usuario'
)
def update(
<<<<<<< HEAD
    user_id: int,
    data: UsuarioPayload, 
    repository: UsuarioRepository = Depends()
):
    service = UsuarioService(repository=repository)
    return service.update(user_id, data)
=======
    data: UpdateUsuarioPayload, 
    repository: EntityRepository = Depends()
) -> dict[str, Any]:
    service = UsuarioController(repository=repository)
    return service.update(data=data)
>>>>>>> main


@router.delete(
    path='/{id}', 
    status_code=HTTPStatus.ACCEPTED,
    summary='Deletar Usuario'
)
<<<<<<< HEAD
def delete(id: str, repository: UsuarioRepository = Depends()):
    return UsuarioService(repository=repository).delete(id=id)
=======
def delete(id: str, repository: EntityRepository = Depends()) -> dict:
    return UsuarioController(repository=repository).delete(id=id)
>>>>>>> main
