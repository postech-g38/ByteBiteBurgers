import pytest


def test_health_check_then_return_success(sync_client):
    # arrange
    # act
    response = sync_client.get('/health_check')
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'alive'
    assert data['message'] == 'hello world'
    