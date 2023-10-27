import pytest


def test_pedido_get_all_pedido_then_return_success(sync_client, create_database, load_database):
    # arrange
    # act
    response = sync_client.get('v1/pedido/')
    # assert
    assert response.status_code == 200


def test_pedido_create_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'produtos': [
            {'produto': 'X-Burger', 'quantidade': 1, 'valor': 10.99}
        ]
    }
    # act
    response = sync_client.post('v1/pedido/', json=payload)
    # assert
    assert response.status_code == 201
    data = response.json()
    assert data['valor'] == 10.99
    

def test_pedido_fake_checkout_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'valor': 10.99,
        'pagamento': 'mercado_pago',
        'produtos': [
            {'produto': 'X-Burger', 'quantidade': 1, 'valor': 10.99}
        ]
    }
    # act
    response = sync_client.post('v1/pedido/checkout', json=payload)
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
