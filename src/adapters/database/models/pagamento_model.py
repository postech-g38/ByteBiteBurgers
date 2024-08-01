from sqlalchemy.orm import Mapped

from src.adapters.database.models.base_model import EntityModel


class PagamentoModel(EntityModel):
    __tablename__ = 'pagamento'

    pedido_id: Mapped[int]
    usuario_id: Mapped[int| None]
    valor: Mapped[float]
    metodo: Mapped[str]
    status: Mapped[str]
    