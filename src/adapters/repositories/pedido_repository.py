from sqlalchemy import select

from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.pedido_model import PedidoModel


class PedidoRepository(SQLAlchemyRepository):
    def __init__(self, database_session) -> None:
        super().__init__(session=database_session)
        self.entity_model = PedidoModel
    
    def get_by_status(self, status: str) -> list:
        stmt = select(self.entity_model).where(self.entity_model.status_pedido == status)
        results = self.session_db.execute(stmt)
        return results.scalars().all()
    