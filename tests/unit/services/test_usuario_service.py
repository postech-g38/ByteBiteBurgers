from unittest.mock import Mock
from datetime import datetime
import uuid

import pytest

from src.services.usuario_service import UsuarioService
from src.adapters.repositories import UsuarioRepository
from src.services.service_base import NotFoundExcepition


def test_usuario_service_get_all_then_raise_not_found_exception():
    # arrange
    repository = Mock(UsuarioRepository)
    repository.get_all.return_value = None
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_all()
    # assert
    repository.get_all.assert_called_once()


@pytest.mark.skip
def test_usuario_service_get_all_then_return_multiple_usuario_entities():
    # arrange
    repository = Mock(UsuarioRepository)
    repository.get_all.return_value = []
    service = UsuarioService(repository)
    # act
    result = service.get_all()
    # assert
    repository.get_all.assert_called_once()


def test_usuario_service_get_by_id_then_raise_not_found_exception():
    # arrange
    usuario_id = 1
    repository = Mock(UsuarioRepository)
    repository.search_by_id.return_value = None
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(usuario_id)
    # assert
    repository.search_by_id.assert_called_once()


def test_usuario_service_get_by_id_then_return_usuario_entity():
    # arrange
    usuario_id = 1
    repository = Mock(UsuarioRepository)
    repository.search_by_id.return_value = {}
    service = UsuarioService(repository)
    # act
    result = service.get_by_id(usuario_id)
    # assert
    repository.search_by_id.assert_called_once_with(usuario_id)
    result is not None


def test_usuario_service_get_by_cpf_then_raise_not_found_exception():
    # arrange
    usuario_cpf = ''
    repository = Mock(UsuarioRepository)
    repository.search_by_cpf.return_value = None
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(usuario_cpf)
    # assert
    repository.search_by_id.assert_called_once_with(usuario_cpf)


def test_usuario_service_get_by_cpf_then_return_usuario_entity():
    # arrange
    usuario_cpf = ''
    repository = Mock(UsuarioRepository)
    repository.search_by_cpf.return_value = {}
    service = UsuarioService(repository)
    # act
    result = service.get_by_id(usuario_cpf)
    # assert
    repository.search_by_id.assert_called_once_with(usuario_cpf)
    assert result is not None


def test_usuario_service_create_usuario_then_return_usuario_entity():
    # arrange
    usuario = {}
    repository = Mock(UsuarioRepository)
    service = UsuarioService(repository)
    # act
    result = service.create(usuario)
    # assert
    assert repository.save.assert_called_once_with(usuario)
    assert repository.refresh.assert_called_once()
    assert isinstance(result.id, uuid)
    assert isinstance(result.created_at, datetime)
    assert isinstance(result.updated_at, datetime)
    assert result.deleted_at is None


@pytest.mark.skip('not implemented')
def test_usuario_service_update_usuario_then_return_usuario_entity():
    # arrange
    usuario_id = 1
    usuario_update = {}
    repository = Mock(UsuarioRepository)
    repository.update.return_value = {}
    service = UsuarioService(repository)
    # act
    result = service.update(usuario_id, usuario_update)
    # assert
    assert repository.update.assert_called_once_with(usuario_id, usuario_update)
    assert repository.refresh.assert_called_once()


@pytest.mark.skip('not implemented')
def test_usuario_service_update_usuario_then_raise_not_found_exception():
    # arrange
    usuario_id = 1
    usuario_update = {}
    repository = Mock(UsuarioRepository)
    repository.update.return_value = None
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.update(usuario_id, usuario_update)
    # assert
    repository.update.assert_called_once_with(usuario_id, usuario_update)
    repository.refresh.assert_called_once()


def test_usuario_service_delete_usuario_then_return_usuario_entity():
    # arrange
    usuario_id = 1
    repository = Mock(UsuarioRepository)
    service = UsuarioService(repository)
    # act
    result = service.delete(usuario_id)
    # assert
    assert repository.save.assert_called_once_with(usuario_id)
    assert repository.refresh.assert_called_once()
    assert isinstance(result.id, uuid)
    assert isinstance(result.created_at, datetime)
    assert isinstance(result.updated_at, datetime)
    assert isinstance(result.deleted_at, datetime)


def test_usuario_service_delete_usuario_then_raise_not_found_exception():
    # arrange
    usuario_id = 1
    repository = Mock(UsuarioRepository)
    repository.delete.return_value = None
    service = UsuarioService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.delete(usuario_id)
    # assert
    repository.delete.assert_called_once_with(usuario_id)
    repository.refresh.assert_called_once()
