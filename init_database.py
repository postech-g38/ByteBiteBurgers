from src.adapters.database.settings import sync_engine
from src.adapters.database.models.carrinho_model import CarrinhoModel
from src.adapters.database.models.categoria_model import CategoriaModel
from src.adapters.database.models.pedido_model import PedidoModel
from src.adapters.database.models.produto_model import ProdutoModel
from src.adapters.database.models.usuario_model import UsuarioModel

CarrinhoModel.metadata.create_all(sync_engine)
CategoriaModel.metadata.create_all(sync_engine)
PedidoModel.metadata.create_all(sync_engine)
ProdutoModel.metadata.create_all(sync_engine)
UsuarioModel.metadata.create_all(sync_engine)