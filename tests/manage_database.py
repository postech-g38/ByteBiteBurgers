import logging

from src.adapters.database.settings import sync_engine, get_session
from src.adapters.database.models.base_model import BaseModel

from tests.manual.database import usuario_model, produto_model
from src.adapters.database.models.usuario_model import UsuarioModel
from src.adapters.database.models.produto_model import ProdutoModel


def database_tables() -> list[str]:
    """List all Models Included on Declarativebase"""
    return BaseModel.metadata.tables.values()

def create_database(tables: list[str]) -> None:
    """Create Database Tables from ORM, EDR will be created too"""
    BaseModel.metadata.create_all(bind=sync_engine, tables=tables, checkfirst=False)

def drop_database(tables: list[str]) -> None:
    """Drop Database Tables"""
    BaseModel.metadata.drop_all(bind=sync_engine, tables=tables, checkfirst=False)

def load_database(database_session, data: list) -> None:
    """Load values on Databse using ORM Models, all values should be passed as Model objects"""
    database_session.add_all(data)


def load_database_mock():
    #ntables = database_tables()
    # drop_database(tables=tables)
    # create_database(tables=tables)

    user_values = [
        UsuarioModel(**usuario_model.USUARIO_MODEL_ADMIN_MOCK),
        UsuarioModel(**usuario_model.USUARIO_MODEL_CLIENTE_MOCK)
    ]

    produto_values = [
        ProdutoModel(**produto_model.PRODUTO_MODEL_BATATA_GRANDE_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_BATATA_MEDIA_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_BURGUER_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_EGG_BURGUER_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_REFRIGERANTE_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_SUCO_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_SORVETE_MOCK),
        ProdutoModel(**produto_model.PRODUTO_MODEL_COOKIES_MOCK)
    ]

    with get_session() as sess:
        load_database(database_session=sess,data=user_values)
        sess.commit()
        sess.flush()
        load_database(database_session=sess,data=produto_values)
        sess.commit()
        sess.flush()
        
    

if __name__ == '__main__':
    load_database_mock()