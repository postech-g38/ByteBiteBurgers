from unittest.mock import patch
from http import HTTPStatus

import pytest

from tests.resouces.database import usuario_model as usuario_mock


@pytest.mark.skip
@pytest.mark.integration_test
def test_usuario_route_paginate_then_return_204_no_content(client):
    # arrange
    params = {'page': 1, 'size': 2, 'order_by': 'created_at:desc'}
    # act
    response = client.get(
        url='/v1/usuario/paginate', 
        headers={'Content-Type': 'application/json'}, 
        params=params
    )
    # assert
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.skip
@pytest.mark.integration_test
def test_usuario_route_paginate_then_return_list(client, database):
    # arrange
    params = {'page': 1, 'size': 2, 'order_by': 'created_at:desc'}
    database.insert_one(usuario_mock.USUARIO_MODEL_CLIENTE_MOCK)
    database.insert_one(usuario_mock.USUARIO_MODEL_CLIENTE_MOCK)
    database.commit()
    # act
    response = client.get(
        url='v1/usuario/paginate', 
        headers={'Content-Type': 'application/json'}, 
        params=params
    )
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.integration_test
def test_usuario_route_find_by_id_then_return_none(client, database):
    # arrange
    usuario_id = '626bccb9697a12204fb22ea3'
    # act
    response = client.get(f"v1/usuario/{usuario_id}")
    # assert
    assert response.status_code == 204


@pytest.mark.integration_test 
def test_usuario_route_find_by_id_then_return_one(client, database):
    # arrange
    usuario_id = '626bccb9697a12204fb22ea3'
    database['usuarios'].insert_one(usuario_mock.USUARIO_MODEL_CLIENTE_MOCK)
    # act
    response = client.get(f"v1/usuario/{usuario_id}")
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.integration_test
def test_usuario_route_create_user_then_return_success(client, database):
    # arrange
    payload = {
        'nome': 'Alguma Pessoa',
        'senha': 'Senha123',
        'cpf': '91487124007',
        'email': 'someone@email.com'
    }
    # act
    response = client.post("/v1/usuario", json=payload)
    # assert
    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.integration_test
def test_usuario_route_update_user_then_return_success(client, database):
    # arrange
    payload = {
        'nome': 'Alguma Pessoa',
        'senha': 'Senha123',
        'cpf': '91487124007'
    }
    # act
    response = client.put("/v1/usuario", json=payload)
    # assert
    assert response.status_code == 202
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.integration_test
def test_usuario_route_create_user_then_return_error(client, database):
    pass


@pytest.mark.integration_test
def test_usuario_route_update_user_then_return_success(client, database):
    pass


@pytest.mark.integration_test
def test_usuario_route_update_user_then_return_error(client, database):
    pass


@pytest.mark.integration_test
def test_usuario_route_delete_user_then_return_success(client, database):
    # arrange
    usuario_id = '626bccb9697a12204fb22ea3'
    database['usuarios'].insert_one(usuario_mock.USUARIO_MODEL_CLIENTE_MOCK)
    # act
    response = client.delete(f"/v1/usuario/{usuario_id}")
    # assert
    assert response.status_code == 202
    data = response.json()
    assert isinstance(data, dict)
