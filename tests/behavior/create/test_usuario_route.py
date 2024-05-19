import pytest
from pytest_bdd import scenarios, given, when, then


# to run the bdd test we should build the app, and get itshost address
# then run pytest tests/behavior
HOST = 'localhost:8000'

scenarios('create.feature')

BASE_URL = f"http://{HOST}/v1"

data = {}


@given('the user payload is prepared')
def prepare_user_payload():
    data['payload'] = {
        'nome': 'someone',
        'senha': 'senha123',
        'cpf': '12345678910',
        'email': 'someone@email.com',
        'tipo': 'cliente'
    }


@when('the user is created')
def create_user(client):
    response = client.post(f"{BASE_URL}/usuario/", json=data['payload'])
    data['response'] = response


@then('the user creation should be successful')
def verify_user_creation():
    assert data['response'].status_code == 201
    data['user_id'] = data['response'].json()['id']


@then('the user should be in the user list')
def verify_user_in_list(client):
    response = client.get(f"{BASE_URL}/usuario/{data['user_id']}")
    assert response.status_code == 200
    user_info = response.json()
    assert user_info['id'] == data['user_id']
    assert user_info['nome'] == data['payload']['nome']
    assert user_info['senha'] == data['payload']['senha']
    assert user_info['cpf'] == data['payload']['cpf']
    assert user_info['email'] == data['payload']['email']
