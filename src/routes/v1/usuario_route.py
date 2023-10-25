from typing import Any, List

from fastapi import APIRouter, Depends

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import EntityRepository
from src.schemas.usuario_schema import CreateUsuarioPayload, ResponseUsuarioPayload, ResponsePagination

router = APIRouter(prefix='/usuario', tags=['Usuario'])


@router.get(
    path='/', 
    response_model=ResponsePagination, 
    tags=['Pegar todos os Usuario']
)
def get_all(repository: EntityRepository = Depends()) -> ResponsePagination:
    return UsuarioService(repository=repository).get_all()


@router.get(
    path='/{id}', 
    # response_model=ResponseUsuarioPayload, 
    tags=['Pegar Usuario']
)
def get(id: int | str, repository: EntityRepository = Depends()):
    service = UsuarioService(repository=repository)
    return service.get(id=id)


@router.get(
    path='/{id}',
    response_model=ResponseUsuarioPayload, 
    tags=['Pegar Usuario']
)
def get(id: int, repository: EntityRepository = Depends()) -> dict:
    service = UsuarioService(repository=repository)
    return service.get(id=id)


@router.get(
    path='/cpf/{cpf}', 
    response_model=ResponseUsuarioPayload, 
    tags=['Pegar Usuario pelo CPF']
)
def get(cpf: str, repository: EntityRepository = Depends()) -> dict:
    service = UsuarioService(repository=repository)
    return service.getByCpf(cpf=cpf)


@router.post(
    path='/criar', 
    response_model=ResponseUsuarioPayload, 
    tags=['Criar Usuario']
)
def create(
    data: CreateUsuarioPayload, 
    repository: EntityRepository = Depends()
) -> dict[str, Any]:
    service = UsuarioService(repository=repository)
    return service.create(data=data)


@router.put(
    path='/atualizar', 
    response_model=ResponseUsuarioPayload, 
    tags=['Atualizar Usuario']
)
def update(
    data: CreateUsuarioPayload, 
    repository: EntityRepository = Depends()
) -> dict[str, Any]:
    service = UsuarioService(repository=repository)
    return service.update(data=data)


@router.delete(
    path='/{id}', 
    response_model=int, 
    tags=['Deletar Usuario']
)
def delete(id: int, repository: EntityRepository = Depends()) -> dict:
    service = UsuarioService(repository=repository)
    return service.delete(id=id)
