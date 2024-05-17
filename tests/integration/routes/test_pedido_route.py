from http import HTTPStatus

import pytest

from src.adapters.database.models.pedido_model import PedidoModel
from tests.resouces.database.pedido_model import PEDIDO_MODEL_LANCHE_MOCK, PEDIDO_MODEL_COMBO_MAKING_MOCK, PEDIDO_MODEL_REFRIGERANTE_MOCK


def test_pedido_route_get_all_then_return_success(client, database):
    # arrange
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.get('/v1/pedido/')
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()


def test_pedido_route_get_by_id_then_return_success(client, database):
    # arrange
    pedido_id = 1
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.get(f"/v1/pedido/{pedido_id}")
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['id'] == pedido_id


def test_pedido_route_update_ten_return_success(client, database):
    # arrange
    pedido_id = 1
    pedido_payload = {
        'valor': 10.99,
        'produtos': [
            {'produto_id': 1, 'quantidade': 1}
        ],
        'status_pedido': 'Recebido',
        'status_pagamento': 'Efetuado',
        'pagamento_id': 'abc'
    }
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.put(f"/v1/pedido/{pedido_id}", json=pedido_payload)
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()


def test_pedido_route_delete_then_return_success(client, database):
    # arrange
    pedido_id = 1
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.delete(f"/v1/pedido/{pedido_id}")
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()


def test_pedido_route_get_by_status_then_return_success(client, database):
    # arrange
    pedido_status = 'recebido'
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.get('/v1/pedido/', params={'status': pedido_status})
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()

@pytest.mark.skip('pedido_id do not exists')
def test_pedido_route_get_pending_orders_then_return_success(client, database):
    # arrange
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    response = client.get('/v1/pedido/pendente')
    print(response.content)
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()  


@pytest.mark.skip
def test_pedido_route_checkout_then_return_success(client, database):
    # arrange
    database.add()
    database.commit()
    # act
    response = client.get('/v1/pedido/checkout')
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()

