from typing import Any

from fastapi import APIRouter, Depends

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import EntityRepository
from src.schemas.usuario import CreateUserPayload

router = APIRouter(prefix='usuario', tags=['Usuario'])


@router.post('/criar')
def create_user(data: CreateUserPayload, repository: EntityRepository = Depends()) -> dict[str, Any]:
    service = UsuarioService(repository=repository)
    return service.create_user()
