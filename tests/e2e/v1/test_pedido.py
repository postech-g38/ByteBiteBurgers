from datetime import datetime

import pytest


def test_pedido_get_all_pedido_then_return_success(sync_client, create_database, load_database):
    # arrange
    # act
    response = sync_client.get('/v1/pedido/')
    # assert
    assert response.status_code == 200


# def test_pedido_create_then_return_success(sync_client, create_database):
#     # arrange
#     payload = {
#         'produtos': [
#             {'produto': 'X-Burger', 'quantidade': 1, 'valor': 10.99}
#         ]
#     }
#     # act
#     response = sync_client.post('/v1/pedido/', json=payload)
#     # assert
#     assert response.status_code == 201
#     data = response.json()
#     assert data['valor'] == 10.99
    

def test_pedido_checkout_then_return_success(sync_client, create_database, load_database):
    # arrange
    payload = {
        'produtos': [
            {'produto_id': 1, 'quantidade': 1}
        ]
    }
    # act
    response = sync_client.post('/v1/pedido/checkout', json=payload)
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 6


def test_pedido_pending_orders_then_return_success(sync_client, create_database, load_database):
    # arrange
    # act
    response = sync_client.get('/v1/pedido/pendente')
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['items'], list)
    assert data['items'][0]['status_pedido'] == 'Recebido'
    assert data['items'][1]['status_pedido'] == 'Recebido'
    assert data['items'][2]['status_pedido'] == 'Em Preparação'
    assert data['items'][3]['status_pedido'] == 'Pronto'
    dt_0 = datetime.strptime(data['items'][0]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
    dt_1 = datetime.strptime(data['items'][1]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
    assert dt_0 >= dt_1
    