from http import HTTPStatus

import pytest


def test_health_check_route_then_return_alive(client):
    # arrange
    # act
    response = client.get('/healthcheck')
    # assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['status'] == 'alive'
    assert data['message'] == 'hello world'
