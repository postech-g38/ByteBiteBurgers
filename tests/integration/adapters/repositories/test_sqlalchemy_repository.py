
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.database.models.pagamento_model import PagamentoModel
from tests.resouces.database import pagamento_model as pagamento_mock 


def test_sqlalchemy_repository_get_all_then_return_list(database):
    # arrange
    database.add(PagamentoModel(**pagamento_mock.PAGAMENTO_CRIADO_MODEL))
    database.add(PagamentoModel(**pagamento_mock.PAGAMENTO_APROVADO_MODEL))
    database.commit()
    repository = PagamentoRepository(database)

    # act
    result = repository.get_all()
    # assert
    print(result)
    assert isinstance(result, list)



def test_sqlalchemy_repository_search_by_id_then_return_value(database):
    # arrange
    usuario_id = 1
    repository = PagamentoRepository(database)
    database.add(PagamentoModel(**pagamento_mock.PAGAMENTO_CRIADO_MODEL))
    database.commit()
    # act
    result = repository.search_by_id(usuario_id)
    # assert
    assert result is not None


def test_sqlalchemy_repository_search_by_id_then_return_none(database):
    # arrange
    usuario_id = 12345
    repository = PagamentoRepository(database)
    # act
    result = repository.search_by_id(usuario_id)
    # assert
    result is None


def test_sqlalchemy_repository_save_then_return_value(database):
    # arrange
    pagamento_model = PagamentoModel(**pagamento_mock.PAGAMENTO_CRIADO_MODEL)
    repository = PagamentoRepository(database)
    # act
    result = repository.save(pagamento_model)
    # assert
    assert result is not None


def test_sqlalchemy_repository_update_then_return_value(database):
    # arrange
    pagamento_id = 1
    pagamento_data = {
        'status': 'cancelado'
    }
    repository = PagamentoRepository(database)
    database.add(PagamentoModel(**pagamento_mock.PAGAMENTO_CRIADO_MODEL))
    database.commit()
    # act
    result = repository.update(pagamento_id, pagamento_data)
    # assert
        