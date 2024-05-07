from sqlalchemy.orm import Mapped

from src.adapters.database.models.base_model import EntityModel


class PagamentoModel(EntityModel):
    pedido_id: Mapped[str]
    usuario_id: Mapped[str]
    valor: Mapped[float]
    metodo: Mapped[str]
    status: Mapped[str]
    