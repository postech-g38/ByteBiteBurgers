from unittest.mock import patch
import json

import pytest
from starlette import status


def test_produto_service_get_all_return_none(sync_client, create_database):
    # arrange
    # act
    response = sync_client.get('v1/produto/')
    # assert
    assert response.status_code == 204


def test_produto_service_get_all_then_return_list(sync_client, create_database, load_database):
    # arrange
    # act
    response = sync_client.get('v1/produto/')
    # assert
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, dict)


def test_produto_service_find_by_id_then_return_none(sync_client, create_database, load_database):
    # arrange
    _id = '10'
    # act
    response = sync_client.get(f"v1/produto/{_id}")
    # assert
    assert response.status_code == 204

    
def test_produto_service_find_by_id_then_return_one(sync_client, create_database, load_database):
    # arrange
    _id = '1'
    # act
    response = sync_client.get(f"/v1/produto/{_id}")
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_produto_service_create_produto_then_return_success(sync_client, create_database):
    # arrange
    payload = {
        'nome': 'Hamburguer Novo',
        'categoria_id': 'lanche',
        'preco': 29.99,
        'imagens': 'path/to/file_1.png',
        'categoria': 'Lanche'
    }
    # act
    response = sync_client.post(
        "/v1/produto", 
        json=payload,
        )
    # assert
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert isinstance(data, dict)



def test_produto_service_create_produto_then_return_error(sync_client, create_database):
    pass


def test_produto_service_update_produto_then_return_success(sync_client, create_database, load_database):
    # arrange
    payload = {
    'id': '1',
    'nome': 'Hamburguer Novo',
    'categoria_id': 'lanche',
    'preco': 29.99,
    'imagens': 'path/to/file_1.png',
    'categoria': 'lanche'
    }
    # act
    response = sync_client.put("/v1/produto/", json=payload)
    # assert
    assert response.status_code == 202
    data = response.json()
    assert isinstance(data, dict)



def test_produto_service_update_produto_then_return_error(sync_client, create_database):
    pass


def test_produto_service_delete_produto_then_return_success(sync_client, create_database, load_database):
    # arrange
    _id = '1'
    # act
    response = sync_client.delete(f"/v1/produto/{_id}")
    # assert
    assert response.status_code == 202
    data = response.json()
    assert isinstance(data, dict)


def test_produto_service_delete_produto_then_return_success(sync_client, create_database):
    pass


@pytest.mark.parametrize('category', ['Lanche', 'Acompanhamento', 'Bebida', 'Sobremesa'])
def test_produto_service_search_by_category_then_return_success(sync_client, create_database, load_database, category):
    # arrange
    # act
    response = sync_client.get(f"/v1/produto/categoria", params={'categoria': category})
    # assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
