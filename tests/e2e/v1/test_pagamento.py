from datetime import datetime

import pytest


def test_pagamento_status_by_order_id_then_return_success(sync_client, create_database, load_database):
    # arrange
    order_id = 1
    # act
    response = sync_client.get(f"/v1/pagamento/pedido/{order_id}")
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data['status_pagamento'] == 'Efetuado'


def test_pagamento_webhook_then_return_success(sync_client, create_database, load_database):
    # arrange
    data = {
        'user_id': 'adsawd',
        'external_pos_id': 'aqwsaw'
    }
    # act
    response = sync_client.post('/v1/pagamento/webhook', json=data)
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'ok'
