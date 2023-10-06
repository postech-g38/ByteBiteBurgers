import pyteest


def test_health_check_then_return_success(sync_client):
    # arrange
    # act
    response = sync_client.get('/health_check')
    # assert
    assert response.status_code == 200
    assert response.json['status'] == 'alive'
    assert response.json['message'] == 'hello world'
    