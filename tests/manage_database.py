import logging

from src.adapters.database.settings import sync_engine, get_session
from src.adapters.database.models.base_model import BaseModel

from tests.resouces.database import usuario_model, produto_model, pedido_model
from src.adapters.database.models.usuario_model import UsuarioModel
from src.adapters.database.models.produto_model import ProdutoModel
from src.adapters.database.models.pedido_model import PedidoModel


def load_database_mock():

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

    pedido_values = [
        PedidoModel(**pedido_model.PEDIDO_MODEL_LANCHE_MOCK),
        PedidoModel(**pedido_model.PEDIDO_MODEL_LANCHE_MOCK),
        PedidoModel(**pedido_model.PEDIDO_MODEL_REFRIGERANTE_MOCK),
        PedidoModel(**pedido_model.PEDIDO_MODEL_COMBO_MOCK),
        PedidoModel(**pedido_model.PEDIDO_MODEL_COMBO_MAKING_MOCK)
    ]

    with get_session() as sess:
        load_database(database_session=sess,data=user_values)
        sess.commit()
        sess.flush()
        load_database(database_session=sess,data=produto_values)
        sess.commit()
        sess.flush()
        load_database(database_session=sess,data=pedido_values)
        sess.commit()
        sess.flush()
        
    

if __name__ == '__main__':
    load_database_mock()