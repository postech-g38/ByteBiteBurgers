



def test_pedido_create_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'cliente_id': 1,
        'items': [
            
        ]
    }
    # act
    response = sync_client.post('/v1/pedido')
    # assert
    assert response.status_code == 201
