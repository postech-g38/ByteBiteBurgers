from unittest.mock import patch

import pytest

from src.services.usuario_service import UsuarioService
from tests.manual.database import usuario_model


def test_usuario_service_get_all_return_none(sync_client, create_database):
    # arrange
    # act
    response = sync_client.get('v1/usuario/')
    # assert
    assert response.status_code == 204


def test_usuario_service_get_all_then_return_list(sync_client, create_database, load_database):
    # arrange
    # act
    response = sync_client.get('v1/usuario/')
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_usuario_service_find_by_id_then_return_none(sync_client, create_database, load_database):
    # arrange
    _id = '10'
    # act
    response = sync_client.get(f"v1/usuario/{_id}")
    # assert
    assert response.status_code == 204

    
def test_usuario_service_find_by_id_then_return_one(sync_client, create_database, load_database):
    # arrange
    _id = '1'
    # act
    response = sync_client.get(f"v1/usuario/{_id}")
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_usuario_service_create_user_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'nome': 'Alguma Pessoa',
        'senha': 'Senha123',
        'cpf': '91487124007',
        'email': 'someone@email.com'
    }
    # act
    response = sync_client.post("/v1/usuario", json=payload)
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_usuario_service_update_user_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'nome': 'Alguma Pessoa',
        'senha': 'Senha123',
        'cpf': '91487124007'
    }
    # act
    response = sync_client.put("/v1/usuario", json=payload)
    # assert
    assert response.status_code == 202
    data = response.json()
    assert isinstance(data, dict)


def test_usuario_service_create_user_then_return_error(sync_client, create_database):
    pass


def test_usuario_service_update_user_then_return_success(sync_client, create_database):
    pass


def test_usuario_service_update_user_then_return_error(sync_client, create_database):
    pass


def test_usuario_service_delete_user_then_return_success(sync_client, create_database):
    pass


def test_usuario_service_delete_user_then_return_success(sync_client, create_database):
    pass
