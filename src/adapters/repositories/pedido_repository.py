from sqlalchemy import select
from sqlalchemy.orm.session import Session
from fastapi import Depends

from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.adapters.database import get_database_session
from src.enums import PedidoStatus


class PedidoRepository(SQLAlchemyRepository):
    def __init__(self, database_session: Session = Depends(get_database_session)) -> None:
        super().__init__(session=database_session)
        self.entity_model = PedidoModel
    
    def get_by_status(self, status: str) -> list[PedidoModel]:
        stmt = select(self.entity_model).where(self.entity_model.status_pedido == status)
        results = self.session_db.execute(stmt)
        return results.scalars().all()
    
    def get_pending_orders(self) -> list[PedidoModel]:
        stmt = select(self.entity_model) \
            .where(self.entity_model.status_pedido != PedidoStatus.FINALIZADO.value)
        results = self.session_db.execute(stmt)
        return results.scalars().all()