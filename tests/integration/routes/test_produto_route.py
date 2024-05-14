from http import HTTPStatus

import pytest

from src.adapters.repositories.produto_repository import ProdutoRepository
from src.services.produto_service import ProdutoService
from src.services.service_base import NotFoundExcepition
from src.adapters.database.models.produto_model import ProdutoModel
from tests.resouces.database.produto_model import PRODUTO_MODEL_BURGUER_MOCK
from src.schemas.produto_schema import CreateProdutoPayload


def test_produto_route_get_all_then_return_success(client, database):
    # arrange
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    response = client.get('/v1/produto/')
    # assert
    assert response.status_code == HTTPStatus.OK
    

def test_produto_route_get_by_id_then_return_success(client, database):
    # arrange
    produto_id = 1
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    response = client.get(f"/v1/produto/{produto_id}")
    # assert
    assert response.status_code == HTTPStatus.OK


def test_produto_route_create_then_return_success(client, database):
    # arrange
    produto_payload = {
        "nome": "X-Burger",
        'preco': 10.99,
        'imagens': 'pth/to/file.png',
        'categoria': 'Lanche'
    }
    # act
    response = client.post('/v1/produto/', json=produto_payload)
    # assert
    assert response.status_code == HTTPStatus.CREATED
        

def test_produto_route_update_then_return_success(client, database):
    # arrange
    produto_id = 1
    produto_payload = {
        "nome": "X-Burger",
        'preco': 10.99,
        'imagens': 'pth/to/file.png',
        'categoria': 'Lanche'
    }
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    response = client.put(f"/v1/produto/{produto_id}", json=produto_payload)
    # assert
    assert response.status_code == HTTPStatus.ACCEPTED
    

def test_produto_route_delete_then_return_success(client, database):
    # arrange
    produto_id = 1
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    response = client.delete(f"/v1/produto/{produto_id}")
    # assert
    assert response.status_code == HTTPStatus.ACCEPTED
    

@pytest.mark.skip
def test_produto_route_get_by_categoria_then_return_success(client, database):
    # arrange
    produto_categoria = 'lanche'
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    response = client.get('/v1/produto/categotia', params={'categoria': produto_categoria})
    # assert
    assert response.status_code == HTTPStatus.OK
    