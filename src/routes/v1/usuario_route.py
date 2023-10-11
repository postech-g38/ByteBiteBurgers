from typing import Any

from fastapi import APIRouter, Depends

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import EntityRepository
from src.schemas.user_schema import CreateUserPayload, ResponseUserPayload

router = APIRouter(prefix='/usuario', tags=['Usuario'])


@router.get(
    path='/{usuario_id}', 
    response_model=ResponseUserPayload, 
    tags=['Pegar Usuario']
)
def create_user(usuario_id: int, repository: EntityRepository = Depends()) -> ResponseUserPayload:
    service = UsuarioService(repository=repository)
    return service.get_user(user_id=usuario_id)


@router.post(
    path='/criar', 
    response_model=ResponseUserPayload, 
    tags=['Criar Usuario']
)
def create_user(data: CreateUserPayload, repository: EntityRepository = Depends()) -> ResponseUserPayload:
    service = UsuarioService(repository=repository)
    return service.create_user(data=data)


@router.put(
    path='/atualizar', 
    response_model=ResponseUserPayload, 
    tags=['Atualizar Usuario']
)
def create_user(data: CreateUserPayload, repository: EntityRepository = Depends()) -> ResponseUserPayload:
    service = UsuarioService(repository=repository)
    return service.update_user(data=data)

