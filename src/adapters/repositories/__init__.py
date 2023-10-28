from fastapi import Depends
from sqlalchemy.orm.session import Session

from src.adapters.database import get_database_session
from src.adapters.repositories.pedido_repository import PedidoRepository
from src.adapters.repositories.produto_repository import ProdutoRepository
from src.adapters.repositories.usuario_repository import UsuarioRepository
from src.adapters.repositories.checkout_repository import CheckoutRepository


class EntityRepository:
    def __init__(self, database: Session = Depends(get_database_session)) -> None:
        self.database_session = database
        self.pedido = PedidoRepository(database_session=database)
        self.produto = ProdutoRepository(database_session=database)
        self.usuario = UsuarioRepository(database_session=database)
        self.checkout = CheckoutRepository(database_session=database)
        