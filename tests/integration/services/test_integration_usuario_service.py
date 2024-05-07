from datetime import datetime
from unittest.mock import Mock

import pytest

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import UsuarioRepository
from src.adapters.database.models import UsuarioModel
from src.services.service_base import NotFoundExcepition
from tests.resouces.database import usuario_model as usuario_mock
from src.schemas.usuario_schema import UsuarioPayload


@pytest.mark.integration_test
@pytest.mark.skip
def test_integragtion_usuario_service_get_all_then_raise_not_found_exception(database):
    # arrange
    # act
    # assert
    pass


@pytest.mark.integration_test
@pytest.mark.skip
def test_integragtion_usuario_service_get_all_then_return_multiple_ususario_entities(database):
    # arrange
    # act
    # assert
    pass


@pytest.mark.integration_test
def test_integration_usuario_service_get_by_id_then_raise_not_found_exception(database):
    # arrange
    usuario_id = 1
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(usuario_id)
    # assert



@pytest.mark.integration_test
def test_integration_usuario_service_get_by_id_then_return_usuario_entity(database):
    # arrange
    usuario_id = 1
    usuario_model = UsuarioModel(
        id=1,
        nome='someone else',
        email='someone@email.com',
        senha='password123',
        cpf='12345678910',
        tipo='admin',
    )
    database.add(usuario_model)
    database.commit()
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    result = service.get_by_id(usuario_id)
    # assert
    result is not None


@pytest.mark.integration_test
def test_integration_usuario_service_get_by_cpf_then_raise_not_found_exception(database):
    # arrange
    usuario_cpf = '12345678910'
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(usuario_cpf)
    # assert


@pytest.mark.integration_test
def test_integration_usuario_service_get_by_cpf_then_return_usuario_entity(database):
    # arrange
    usuario_cpf = '12345678910'
    usuario_model = UsuarioModel(
        id=1,
        nome='someone else',
        email='someone@email.com',
        senha='password123',
        cpf=usuario_cpf,
        tipo='admin',
    )
    database.add(usuario_model)
    database.commit()
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    result = service.get_by_cpf(usuario_cpf)
    # assert


@pytest.mark.integration_test
def test_integration_usuario_service_create_usuario_then_return_usuario_entity(database):
    # arrange
    usuario_payload = UsuarioPayload(
        nome='someone else',
        email='someone@email.com',
        senha='password123',
        cpf='12345678910',
        tipo='admin',
    )
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    result = service.create(usuario_payload)
    # assert
    assert result.id == 1
    assert isinstance(result.created_at, datetime)
    assert result.updated_at is None
    assert result.deleted_at is None
    assert result.nome == 'someone else'
    assert result.email == 'someone@email.com'
    assert result.senha == 'password123'
    assert result.cpf == '12345678910'
    assert result.tipo == 'admin'


@pytest.mark.integration_test
def test_integration_usuario_service_update_usuario_then_return_usuario_entity(database):
    # arrange
    usuario_id = 1
    usuario_model = UsuarioModel(
        nome='someone else',
        email='someone@email.com',
        senha='password123',
        cpf='12345678910',
        tipo='admin',
    )
    database.add(usuario_model)
    database.commit()
    usuario_update = {
        'nome': 'anything else'
    }
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    result = service.update(usuario_id, usuario_update)
    # assert
    assert result.id == usuario_id
    assert isinstance(result.created_at, datetime)
    # assert isinstance(result.updated_at, datetime)
    # assert result.created_at <= result.updated_at
    assert result.updated_at is None
    assert result.deleted_at is None


@pytest.mark.integration_test
def test_integration_usuario_service_update_usuario_then_raise_not_found_exception(database):
    # arrange
    usuario_id = 1
    usuario_update = {
        'nome': 'anything else'
    }
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.update(usuario_id, usuario_update)
    # assert


@pytest.mark.integration_test
def test_integration_usuario_service_delete_usuario_then_return_usuario_entity(database):
    # arrange
    usuario_id = 1
    usuario_model = UsuarioModel(
        id=usuario_id,
        nome='someone else',
        email='someone@email.com',
        senha='password123',
        cpf='12345678910',
        tipo='admin',
    )
    database.add(usuario_model)
    database.commit()
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    result = service.delete(usuario_id)
    # assert
    assert result.id == 1
    assert isinstance(result.created_at, datetime)
    assert result.updated_at is None
    assert isinstance(result.deleted_at, datetime)
    # assert result.created_at < result.deleted_at


@pytest.mark.integration_test
def test_integration_usuario_service_delete_usuario_then_raise_not_found_exception(database):
    # arrange
    usuario_id = 1
    repository = UsuarioRepository(database)
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.delete(usuario_id)
    # assert

