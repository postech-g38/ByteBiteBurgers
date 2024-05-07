import pytest


def test_route_healthcheck_then_return_alive(client):
    # arrange
    # act
    result = client.get('/healthcheck')
    # assert
    assert result.status_code == 200
    data = result.json()
    assert data['status'] == 'alive'
    assert data['message'] == 'hello world'
